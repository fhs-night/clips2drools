(defrule SportLevelConfirm
(SportType ?SportType)
(BMI ?BMI)
=>
(if(or(eq ?SportType NO) (eq ?SportType SICKBED))
then
(bind ?SportLevel 25)
)
(if(<= ?BMI 20)
then
(bind ?SportLevel (+ ?SportLevel 5))
)
(OperateNumberFact "SportLevel" ?SportLevel)
)