(deffunction FourInFiveOut (?InputNum)
(bind ?Integer (div ?InputNum 1))
(bind ?BelowPoint (- ?InputNum ?Integer))
(if
	(<= ?BelowPoint 0.25)
	then
	(bind ?Result ?Integer)
	else
	(if (and (> ?BelowPoint 0.25) (<= ?BelowPoint 0.75))
		then
		(bind ?Result (+ ?Integer 0.5))
		else
		(bind ?Result (+ ?Integer 1))
	)
)
(return ?Result)
)
;���ȿ�����ȷ��
(defrule SportLevelConfirm
(SportType ?SportType)
(BMI ?BMI)
=>
(if(or(eq ?SportType NO) (eq ?SportType SICKBED))
then
(bind ?SportLevel 25)
)

(if(or(eq ?SportType FREEDEGREE) (eq ?SportType LOWDEGREE))
then
(bind ?SportLevel 30)
)

(if(or(eq ?SportType MIDDLEDEGREE) (eq ?SportType HIGHDEGREE))
then
(bind ?SportLevel 35)
)

(if(>= ?BMI 25)
then
(bind ?SportLevel (- ?SportLevel 5))
)

; (printout t "SportLevel = " ?SportLevel crlf)
;(assert (SportLevel ?SportLevel))
(OperateNumberFact "SportLevel" ?SportLevel)
)

(defrule IdealBMIConfirm
(Height ?Height)
=>
(bind ?Height (/ ?Height 100))
(if(< ?Height 1.50)
then
(bind ?IdealBMI 21)
)

(if(and (>= ?Height 1.50) (< ?Height 1.65))
then
(bind ?IdealBMI 22)
)

(if(and (>= ?Height 1.65) (< ?Height 1.85))
then
(bind ?IdealBMI 23)
)

(if(>= ?Height 1.85)
then
(bind ?IdealBMI 24)
)
;(printout t "IdealBMI = " ?IdealBMI crlf)

;(assert (IdealBMI ?IdealBMI))
(OperateNumberFact "IdealBMI" ?IdealBMI)
)



(defrule SexCoeffConfirm
(Sex ?Sex)
=>
(if(eq ?Sex male)
then
(bind ?SexCoeff 1)
)

(if(eq ?Sex female)
then
(bind ?SexCoeff 0.95)
)
;(printout t "SexCoeff = " ?SexCoeff crlf)
;(assert (SexCoeff ?SexCoeff))
(OperateNumberFact "SexCoeff" ?SexCoeff)
)

(defrule AgeCoeffConfirm
(Age ?Age)
=>
(if(< ?Age 25)
then
(bind ?AgeCoeff 1.05)
)

(if(and (>= ?Age 25) (< ?Age 55))
then
(bind ?AgeCoeff 1.00)
)

(if(and (>= ?Age 55) (< ?Age 65))
then
(bind ?AgeCoeff 0.95)
)

(if(and (>= ?Age 65) (< ?Age 75))
then
(bind ?AgeCoeff 0.90)
)

(if(and (>= ?Age 75) (< ?Age 85))
then
(bind ?AgeCoeff 0.85)
)

(if(>= ?Age 85)
then
(bind ?AgeCoeff 0.80)
)
;(printout t "AgeCoeff = " ?AgeCoeff crlf)
;(assert (AgeCoeff ?AgeCoeff))
(OperateNumberFact "AgeCoeff" ?AgeCoeff)
)

(defrule DiseaseStatusCoeffConfirm
(DiseaseStatus ?DiseaseStatus)
=>
(if(eq ?DiseaseStatus COMMON)
then
(bind ?DiseaseStatusCoeff 1.00)
)

(if(eq ?DiseaseStatus SPECIAL)
then
(bind ?DiseaseStatusCoeff 1.05)
)
;(printout t "DiseaseStatusCoeff = " ?DiseaseStatusCoeff crlf)
;(assert (DiseaseStatusCoeff ?DiseaseStatusCoeff))
(OperateNumberFact "DiseaseStatusCoeff" ?DiseaseStatusCoeff)
)

(defrule TKcalCalc
(SportLevel ?SportLevel)
(IdealBMI ?IdealBMI)
(Height ?Height)
(SexCoeff ?SexCoeff)
(AgeCoeff ?AgeCoeff)
(DiseaseStatusCoeff ?DiseaseStatusCoeff)
=>
(bind ?Height (/ ?Height 100))
(bind ?TKcal (* (* (* (* (* (* ?SportLevel ?IdealBMI) ?Height) ?Height) ?SexCoeff) ?AgeCoeff) ?DiseaseStatusCoeff) )
(bind ?TKcal (* (div ?TKcal 5) 5))
;(printout t "���ȿ�Ϊ = " ?TKcal crlf)
;(assert (TKcal ?TKcal))
(OperateNumberFact "TKcal" ?TKcal)
)

;ʳ��������
(defrule Protein_Carbo_Fat_AmountCalc
(Dyslipidemia_Diagnose_TG ?Dyslipidemia_Diagnose_TG)
(Dyslipidemia_Diagnose_TC ?Dyslipidemia_Diagnose_TC)
(Sex ?Sex)
(Age ?Age)
(Weight ?Weight)
(Cr_Variable ?Cr_Variable)
(ACr_Variable ?ACr_Variable)
(IdealBMI ?IdealBMI)
(Height ?Height)
(TKcal ?TKcal)
(UrineProtein ?UrineProtein)
(HUA_Diagnose ?HUA_Diagnose)
(DM_History ?DM_History)
(DM_Diagnose ?DM_Diagnose)
(HUA_Diagnose ?HUA_Diagnose)
(Hypertension_Diagnose ?Hypertension_Diagnose)
=>
(bind ?DietaryType "F")
(if (or (eq ?DM_History YES)(eq ?DM_Diagnose IGT) 
(eq ?DM_Diagnose IFG) (eq ?DM_Diagnose T1DM) 
(eq ?DM_Diagnose T2DM)(eq ?DM_Diagnose DM) 
(eq ?DM_Diagnose DM_NoneType)(eq ?DM_Diagnose IGR))
then
(bind ?DietaryType(str-cat ?DietaryType "1"))
)

(if (eq ?HUA_Diagnose Hyperuricaemia)
then
(bind ?DietaryType(str-cat ?DietaryType "4"))
)

(if (eq ?Hypertension_Diagnose Hypertension)
then
(bind ?DietaryType(str-cat ?DietaryType "3"))
)

(bind ?Height (/ ?Height 100))
(if(eq ?Dyslipidemia_Diagnose_TG Dyslipidemia_TG)
then
(bind ?FatAmount_Temp 20)
(bind ?CarboRatioLimit 55)
;(Recommendation "�ɸɹ�")
(OperateFact "Nut" YES)
(bind ?DietaryType(str-cat ?DietaryType "2"))
else
(bind ?FatAmount_Temp 30)
(bind ?CarboRatioLimit 50)
(OperateFact "Nut" NO)
)

(if(eq ?Dyslipidemia_Diagnose_TC Dyslipidemia_TC)
then
;(printout t "��ʳ��������" crlf)
(Recommendation "��ʳ��������")
(bind ?DietaryType(str-cat ?DietaryType "5"))
)

(OperateFact "DietaryType" ?DietaryType)

(bind ?BaseProteinAmount 1.2)
(if(eq ?Sex male)
then
(bind ?Ccr (div (* (* (- 140 ?Age) ?Weight) 1.228) ?Cr_Variable))
)

(if(eq ?Sex female)
then
(bind ?Ccr (div (* (* (- 140 ?Age) ?Weight) 1.04) ?Cr_Variable))
)
;(assert (Ccr ?Ccr))
;(printout t "Ccr = " ?Ccr crlf)
(OperateNumberFact "Ccr" ?Ccr)

(if(< ?Ccr 80)
then
(bind ?BaseProteinAmount (- ?BaseProteinAmount 0.2))
)

(if(or (eq ?HUA_Diagnose Hyperuricaemia) (and(> ?ACr_Variable 30)  (< ?ACr_Variable 300)) (and (> ?UrineProtein 0.15) (< ?UrineProtein 3.5)) )
;reivsed by wbf 081229 �򵰰׶�����λ��mg/��ת��Ϊg/��
then
(bind ?BaseProteinAmount (- ?BaseProteinAmount 0.2))
)

(if(or (< ?Ccr 50) (>= ?ACr_Variable 300) (>= ?UrineProtein 3.5))
;reivsed by wbf 081229 �򵰰׶�����λ��mg/��ת��Ϊg/��
then
(bind ?BaseProteinAmount (- ?BaseProteinAmount 0.2))
)

(if(< ?Ccr 10)
then
(bind ?BaseProteinAmount (- ?BaseProteinAmount 0.2))
)
;(printout t "BaseProteinAmount = " ?BaseProteinAmount crlf)

(if(eq ?HUA_Diagnose Hyperuricaemia) 
then
;(printout t "��������ʳ����ֲ�ﵰ�ף�" crlf)
(Recommendation "��������ʳ����ֲ�ﵰ�ף�")
)

(if(< ?Ccr 50) 
then
;(printout t "�����ʵ���" crlf)
(Recommendation "�����ʵ���")
)

(if(< ?Ccr 10) 
then
;(printout t "����aͪ��" crlf)
(Recommendation "����aͪ��")
)
(assert (BaseProteinAmount ?BaseProteinAmount))
(bind ?ProteinAmount_Temp (* (* (* ?BaseProteinAmount ?IdealBMI) ?Height) ?Height))
(assert (ProteinAmount_Temp ?ProteinAmount_Temp))
(bind ?ProteinRatio_Temp (div (* ?ProteinAmount_Temp 1000) ?TKcal)) 
(assert (ProteinRatio_Temp ?ProteinRatio_Temp))

(if(<= ?ProteinRatio_Temp 30)
then
(bind ?ProteinRatio ?ProteinRatio_Temp)
(bind ?ProteinAmount ?ProteinAmount_Temp)
else
(bind ?ProteinRatio 30)
(bind ?ProteinAmount (* ?TKcal 0.03))
)
(bind ?TKProtein (div (* ?ProteinRatio ?TKcal) 100))

;(printout t "�����ʱ��� = " ?ProteinRatio crlf)
;(assert (ProteinRatio ?ProteinRatio))
(OperateNumberFact "ProteinRatio" ?ProteinRatio)
;(bind ?ProteinAmount (div ?ProteinAmount 1))
;(printout t "�����ʿ�ʳ���� = " ?ProteinAmount crlf)
(OperateNumberFact "ProteinAmount" ?ProteinAmount)

(bind ?CarboRatio_Temp (- (- 100 ?ProteinRatio) (div (* ?FatAmount_Temp 9) ?TKcal)))

(if(<= ?CarboRatio_Temp ?CarboRatioLimit)
then
(bind ?CarboRatio ?CarboRatio_Temp)
(bind ?CarboAmount (div (- (- ?TKcal (div (* ?ProteinRatio ?TKcal) 100)) (* ?FatAmount_Temp 9)) 4))
else
(bind ?CarboRatio ?CarboRatioLimit)
(bind ?CarboAmount (div (* ?CarboRatioLimit ?TKcal) 400))
)
(bind ?TKCarbo (div (* ?CarboRatio ?TKcal) 100))

;(printout t "������� = " ?CarboRatio crlf)
;(assert (CarboRatio ?CarboRatio))
(OperateNumberFact "CarboRatio" ?CarboRatio)
;(bind ?CarboAmount (* 5 (div ?CarboAmount 5)))
;(printout t "�����ʳ���� = " ?CarboAmount crlf)
;(assert (CarboAmount ?CarboAmount))
(OperateNumberFact "CarboAmount" ?CarboAmount)

(bind ?FatRatio (- (- 100 ?CarboRatio) ?ProteinRatio))
(bind ?FatAmount (div (* ?FatRatio ?TKcal) 900))
(bind ?TKFat (div (* ?FatRatio ?TKcal) 100))
;(printout t "֬������ = " ?FatRatio crlf)
;(assert (FatRatio ?FatRatio))
(OperateNumberFact "FatRatio" ?FatRatio)
;(printout t "֬����ʳ���� = " ?FatAmount crlf)
;(assert (FatAmount ?FatAmount))
(OperateNumberFact "FatAmount" ?FatAmount)

(bind ?MeatAmount (* (- (- ?ProteinAmount (* ?CarboAmount 0.07)) 15.75) 5.556))
(bind ?MeatAmount (* 5 (div ?MeatAmount 5)))
;(printout t "�����ʳ���� = " ?MeatAmount crlf)
;(assert (MeatAmount ?MeatAmount))
(OperateNumberFact "MeatAmount" ?MeatAmount)

;(assert (MilkAmount 250))
;(printout t "ţ��ʳ���� = " 250 crlf)
(OperateNumberFact "MilkAmount" 250)

;(assert (EggAmount 1))
;(printout t "�������� = " 1 crlf)
(OperateNumberFact "EggAmount" 1)

(bind ?TotalCarboWithoutFruit (- (/ (* ?CarboAmount 4) 90) 1) )
(bind ?MainFood ?TotalCarboWithoutFruit)
;(printout t "��ʳ�� = " ?MainFood crlf)
(bind ?MainFood (FourInFiveOut ?MainFood))
;(assert (MainFood ?MainFood))
(OperateNumberFact "MainFood" ?MainFood)

(bind ?Fruit 1)
;(printout t "ˮ���� = " ?Fruit crlf)
;(bind ?Fruit (FourInFiveOut ?Fruit))
;(assert (Fruit ?Fruit))
(OperateNumberFact "Fruit" ?Fruit)

;(bind ?Vegetable (* ?MainFood 0.25))
;(if(< ?Vegetable 1)
;then
;(bind ?Vegetable 1)
;)
;(printout t "�߲˷� = " ?Vegetable crlf)
;(assert (Vegetable ?Vegetable))
(bind ?Vegetable (FourInFiveOut 1))
(OperateNumberFact "Vegetable" ?Vegetable)

(bind ?TotalCarbo (+ (+ ?MainFood ?Fruit) ?Vegetable))
(OperateNumberFact "TotalCarbo" ?TotalCarbo)

(bind ?Meat (/ ?MeatAmount 50) )
;(printout t "����� = " ?Meat crlf)
;(assert (Meat ?Meat))
(bind ?Meat (FourInFiveOut ?Meat))
(OperateNumberFact "Meat" ?Meat)

(bind ?TotalProtein (+ ?Meat 2.5))
(OperateNumberFact "TotalProtein" ?TotalProtein)

(bind ?TotalFat (/ ?FatAmount 10))
(bind ?TotalFat (FourInFiveOut ?TotalFat))
;(printout t "֬���� = " ?TotalFat crlf)
;(assert (TotalFat ?TotalFat))
(OperateNumberFact "TotalFat" ?TotalFat)

;(printout t "ʳ���ͷ� = " ?TotalFat crlf)
;(assert (Oil ?TotalFat))
(OperateNumberFact "Oil" ?TotalFat)


)

;ˮ�ζ���
(defrule WaterAndSaltConfirm
(Fat_Diagnose ?Fat_Diagnose)
(Weight ?Weight)
(Hypertension_Diagnose ?Hypertension_Diagnose)
(Ccr ?Ccr)
=>
(bind ?MaxWater (* ?Weight 40))
(bind ?MinWater (* ?Weight 30))

(if(<= ?Ccr 30)
then
(bind ?MaxWater (* ?MaxWater 0.8))
(bind ?MaxWater (* 100 (div ?MaxWater 100)))
(bind ?MinWater (* ?MinWater 0.8))
(bind ?MinWater (* 100 (div ?MinWater 100)))
)
;(printout t "ʳ��ˮ" ?MinWater"~" ?MaxWater "ml/��" crlf)
;(assert (MaxWater ?MaxWater))
;(assert (MinWater ?MinWater))
(OperateNumberFact "MaxWater" ?MaxWater)
(OperateNumberFact "MinWater" ?MinWater)

(if(<= ?Ccr 30)
then
(bind ?Salt 5)
else
(if(or (eq ?Hypertension_Diagnose Hypertension) (eq ?Fat_Diagnose Fat))
then
(bind ?Salt 6)
else
(bind ?Salt 8)
)
)

;(printout t "ʳ����" ?Salt "g/��" crlf)
;(assert (Salt ?Salt))
(OperateNumberFact "Salt" ?Salt)
;(undefrule *)
;add by wbf 081230��ֹ�����ظ�����
)