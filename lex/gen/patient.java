package com.sample;

public class Patient {

public String filepath;
public String DM_Diagnose_EVENT;
public String DM_Therapy_EVENT;
public String Dyslipidemia_Diagnose_EVENT;
public String Dyslipidemia_TC_EVENT;
public String Dyslipidemia_TG_EVENT;
public String Dyslipidemia_LDLC_EVENT;
public String Dyslipidemia_HDLC_EVENT;
public String Fat_Diagnose_EVENT;
public String Hyperuricaemia_Diagnose_EVENT;
public String Hyperuricaemia_Therapy_EVENT;
public String Hypertension_Diagnose_EVENT;
public String Hypertension_Therapy_Suggestion_EVENT;
public String Hypertension_Therapy_EVENT;
public String MS_Evaluate_Event;
public String DM_SelfMonitor_Event;
public String Dyslipidemia_SelfMonitor_EVENT;
public String HUA_SelfMonitor_EVENT;
public String Antiplatelet_Drug_Use_EVENT;
public String Fat_Therapy_EVENT;
public String SportType;
public double BMI;
public double SportLevel;
public double Height;
public double IdealBMI;
public String Sex;
public double SexCoeff;
public double Age;
public double AgeCoeff;
public String DiseaseStatus;
public double DiseaseStatusCoeff;
public double TKcal;
public String Dyslipidemia_Diagnose_TG;
public String Dyslipidemia_Diagnose_TC;
public double Weight;
public double Cr_Variable;
public double ACr_Variable;
public double UrineProtein;
public String DM_History;
public String DM_Diagnose;
public String HUA_Diagnose;
public String Hypertension_Diagnose;
public String Nut;
public String DietaryType;
public double Ccr;
public double BaseProteinAmount;
public double ProteinAmount_Temp;
public double ProteinRatio_Temp;
public double ProteinRatio;
public double ProteinAmount;
public double CarboRatio;
public double CarboAmount;
public double FatRatio;
public double FatAmount;
public double MeatAmount;
public double MilkAmount;
public double EggAmount;
public double MainFood;
public double Fruit;
public double Vegetable;
public double TotalCarbo;
public double Meat;
public double TotalProtein;
public double TotalFat;
public double Oil;
public String Fat_Diagnose;
public double MaxWater;
public double MinWater;
public double Salt;
public String T1DMHis;
public String T2DMHis;
public double HbA1c;
public double FBG_Variable;
public double twoHPBG_Variable;
public String Fat_History;
public String DM_Family_History;
public String GDM_History;
public String Macrosomia_History;
public String ICA;
public String GAD65;
public double FBG_OGTT_Variable;
public double twoHPBG_OGTT_Variable;
public String statins_Drug;
public String LDLch_Reach_Standard;
public String LDLch_First_Drug;
public double risk_score;
public double LDLch_Variable;
public double TC_Variable;
public double HDLch_Variable;
public String Dyslipidemia_Drug;
public String HDLch_First_Drug;
public String HDLch_Reach_Standard;
public String fibrates_Drug;
public double TG_Variable;
public String TG_First_Drug;
public String TG_Reach_Standard;
public String Dyslipidemia_Diagnose_HDLC;
public String Dyslipidemia_Diagnose_LDLC;
public String Dyslipidemia_Diagnosed;
public String Dyslipidemia_History;
public String Dyslipidemia_TG_His;
public String Dyslipidemia_TC_His;
public String Dyslipidemia_HDLch_His;
public String Dyslipidemia_LDLch_His;
public double waistline_Variable;
public String Acute_Gouty_Arthritis_History;
public String Hyperuricaemia_History;
public String arthritis_flare;
public String HUA_Diagnose_Acute;
public double UA_Variable;
public String HUA_Diagnose_PS;
public String UA_Down_drug;
public String Acute_Gouty_Arthritis_Period;
public double UUA;
public String abnormal_renal_function;
public String Gout_History;
public String HUA_Diagnose_Gouty;
public double UPh;
public String Malignant_Tumour;
public String Chemotherapy;
public String Nephropathy;
public String Dose_Affect_UA_Excretion;
public String Cerebrovascular_Disease_History;
public double SBP_Current_Variable;
public double DBP_Current_Variable;
public String HT_Down_drug;
public String hypertension_Diagnose_Stage;
public double heart_rate;
public String irenal_artery_Bistenosis;
public String DM_kidney;
public String renal_artery_stenosis;
public String Hypertension_Diagnose_PS;
public double DBP_Top_Variable;
public double SBP_Top_Variable;
public String Cardiopathy_History;
public String Peripheral_Vascular_Disease_History;
public String Retinopathy_History;
public String Hyperuricaemia_Diagnose_risklevel;
public String smoke_history;
public String Cardiovascular_Disease_Family_History;
public String lack_of_exercise;
public String Hypertension_History;
public String Metabolic_Syndrome_Conclude;
public String Hypertension_Family_History;
public String Dyslipidemia_Family_History;
public String Hyperuricemia_Family_History;
public String Coronary_Heart_Disease_Family_History;
public String Cerebral_Infarct_Family_History;
public String Cerebral_Infarct;
public String Lower_Extremity_Angiopathy;
public String MSRiskDegree;
public String IFGHis;
public String IGTHis;
public String IGRHis;
public String DM_Drug;
public String Insolin;
public String Shuanggua_Drug;
public String Gelienai_Drug;
public String Gelietong_Drug;
public String Huangniao_Drug;
public String AGI_Drug;
public String TC_Reach_Standard;
public String TC_First_Drug;
public String GlucoseLevel;
public String GLByFBGA;
public String GLByRBGA;
public double BG_Variable;
public String ReduceWeight;
public String ReduceBG;
public String StrengthenPhysique;
public double ReduceBGCal;
public double ReduceWeightCal;
public String LimbDyskinesia;
public String SportTypeLow;
public String SportTypeMiddle;
public String SportTypeHigh;
public double LEnergyConsumption;
public double MEnergyConsumption;
public double HEnergyConsumption;

public void setfilepath(String filepath){
this.filepath = filepath;
}

public String getfilepath(){
return this.filepath;
}

public void setDM_Diagnose_EVENT(String DM_Diagnose_EVENT){
this.DM_Diagnose_EVENT = DM_Diagnose_EVENT;
}

public String getDM_Diagnose_EVENT(){
return this.DM_Diagnose_EVENT;
}

public void setDM_Therapy_EVENT(String DM_Therapy_EVENT){
this.DM_Therapy_EVENT = DM_Therapy_EVENT;
}

public String getDM_Therapy_EVENT(){
return this.DM_Therapy_EVENT;
}

public void setDyslipidemia_Diagnose_EVENT(String Dyslipidemia_Diagnose_EVENT){
this.Dyslipidemia_Diagnose_EVENT = Dyslipidemia_Diagnose_EVENT;
}

public String getDyslipidemia_Diagnose_EVENT(){
return this.Dyslipidemia_Diagnose_EVENT;
}

public void setDyslipidemia_TC_EVENT(String Dyslipidemia_TC_EVENT){
this.Dyslipidemia_TC_EVENT = Dyslipidemia_TC_EVENT;
}

public String getDyslipidemia_TC_EVENT(){
return this.Dyslipidemia_TC_EVENT;
}

public void setDyslipidemia_TG_EVENT(String Dyslipidemia_TG_EVENT){
this.Dyslipidemia_TG_EVENT = Dyslipidemia_TG_EVENT;
}

public String getDyslipidemia_TG_EVENT(){
return this.Dyslipidemia_TG_EVENT;
}

public void setDyslipidemia_LDLC_EVENT(String Dyslipidemia_LDLC_EVENT){
this.Dyslipidemia_LDLC_EVENT = Dyslipidemia_LDLC_EVENT;
}

public String getDyslipidemia_LDLC_EVENT(){
return this.Dyslipidemia_LDLC_EVENT;
}

public void setDyslipidemia_HDLC_EVENT(String Dyslipidemia_HDLC_EVENT){
this.Dyslipidemia_HDLC_EVENT = Dyslipidemia_HDLC_EVENT;
}

public String getDyslipidemia_HDLC_EVENT(){
return this.Dyslipidemia_HDLC_EVENT;
}

public void setFat_Diagnose_EVENT(String Fat_Diagnose_EVENT){
this.Fat_Diagnose_EVENT = Fat_Diagnose_EVENT;
}

public String getFat_Diagnose_EVENT(){
return this.Fat_Diagnose_EVENT;
}

public void setHyperuricaemia_Diagnose_EVENT(String Hyperuricaemia_Diagnose_EVENT){
this.Hyperuricaemia_Diagnose_EVENT = Hyperuricaemia_Diagnose_EVENT;
}

public String getHyperuricaemia_Diagnose_EVENT(){
return this.Hyperuricaemia_Diagnose_EVENT;
}

public void setHyperuricaemia_Therapy_EVENT(String Hyperuricaemia_Therapy_EVENT){
this.Hyperuricaemia_Therapy_EVENT = Hyperuricaemia_Therapy_EVENT;
}

public String getHyperuricaemia_Therapy_EVENT(){
return this.Hyperuricaemia_Therapy_EVENT;
}

public void setHypertension_Diagnose_EVENT(String Hypertension_Diagnose_EVENT){
this.Hypertension_Diagnose_EVENT = Hypertension_Diagnose_EVENT;
}

public String getHypertension_Diagnose_EVENT(){
return this.Hypertension_Diagnose_EVENT;
}

public void setHypertension_Therapy_Suggestion_EVENT(String Hypertension_Therapy_Suggestion_EVENT){
this.Hypertension_Therapy_Suggestion_EVENT = Hypertension_Therapy_Suggestion_EVENT;
}

public String getHypertension_Therapy_Suggestion_EVENT(){
return this.Hypertension_Therapy_Suggestion_EVENT;
}

public void setHypertension_Therapy_EVENT(String Hypertension_Therapy_EVENT){
this.Hypertension_Therapy_EVENT = Hypertension_Therapy_EVENT;
}

public String getHypertension_Therapy_EVENT(){
return this.Hypertension_Therapy_EVENT;
}

public void setMS_Evaluate_Event(String MS_Evaluate_Event){
this.MS_Evaluate_Event = MS_Evaluate_Event;
}

public String getMS_Evaluate_Event(){
return this.MS_Evaluate_Event;
}

public void setDM_SelfMonitor_Event(String DM_SelfMonitor_Event){
this.DM_SelfMonitor_Event = DM_SelfMonitor_Event;
}

public String getDM_SelfMonitor_Event(){
return this.DM_SelfMonitor_Event;
}

public void setDyslipidemia_SelfMonitor_EVENT(String Dyslipidemia_SelfMonitor_EVENT){
this.Dyslipidemia_SelfMonitor_EVENT = Dyslipidemia_SelfMonitor_EVENT;
}

public String getDyslipidemia_SelfMonitor_EVENT(){
return this.Dyslipidemia_SelfMonitor_EVENT;
}

public void setHUA_SelfMonitor_EVENT(String HUA_SelfMonitor_EVENT){
this.HUA_SelfMonitor_EVENT = HUA_SelfMonitor_EVENT;
}

public String getHUA_SelfMonitor_EVENT(){
return this.HUA_SelfMonitor_EVENT;
}

public void setAntiplatelet_Drug_Use_EVENT(String Antiplatelet_Drug_Use_EVENT){
this.Antiplatelet_Drug_Use_EVENT = Antiplatelet_Drug_Use_EVENT;
}

public String getAntiplatelet_Drug_Use_EVENT(){
return this.Antiplatelet_Drug_Use_EVENT;
}

public void setFat_Therapy_EVENT(String Fat_Therapy_EVENT){
this.Fat_Therapy_EVENT = Fat_Therapy_EVENT;
}

public String getFat_Therapy_EVENT(){
return this.Fat_Therapy_EVENT;
}

public void setSportType(String SportType){
this.SportType = SportType;
}

public String getSportType(){
return this.SportType;
}

public void setBMI(double BMI){
this.BMI = BMI;
}

public double getBMI(){
return this.BMI;
}

public void setSportLevel(double SportLevel){
this.SportLevel = SportLevel;
}

public double getSportLevel(){
return this.SportLevel;
}

public void setHeight(double Height){
this.Height = Height;
}

public double getHeight(){
return this.Height;
}

public void setIdealBMI(double IdealBMI){
this.IdealBMI = IdealBMI;
}

public double getIdealBMI(){
return this.IdealBMI;
}

public void setSex(String Sex){
this.Sex = Sex;
}

public String getSex(){
return this.Sex;
}

public void setSexCoeff(double SexCoeff){
this.SexCoeff = SexCoeff;
}

public double getSexCoeff(){
return this.SexCoeff;
}

public void setAge(double Age){
this.Age = Age;
}

public double getAge(){
return this.Age;
}

public void setAgeCoeff(double AgeCoeff){
this.AgeCoeff = AgeCoeff;
}

public double getAgeCoeff(){
return this.AgeCoeff;
}

public void setDiseaseStatus(String DiseaseStatus){
this.DiseaseStatus = DiseaseStatus;
}

public String getDiseaseStatus(){
return this.DiseaseStatus;
}

public void setDiseaseStatusCoeff(double DiseaseStatusCoeff){
this.DiseaseStatusCoeff = DiseaseStatusCoeff;
}

public double getDiseaseStatusCoeff(){
return this.DiseaseStatusCoeff;
}

public void setTKcal(double TKcal){
this.TKcal = TKcal;
}

public double getTKcal(){
return this.TKcal;
}

public void setDyslipidemia_Diagnose_TG(String Dyslipidemia_Diagnose_TG){
this.Dyslipidemia_Diagnose_TG = Dyslipidemia_Diagnose_TG;
}

public String getDyslipidemia_Diagnose_TG(){
return this.Dyslipidemia_Diagnose_TG;
}

public void setDyslipidemia_Diagnose_TC(String Dyslipidemia_Diagnose_TC){
this.Dyslipidemia_Diagnose_TC = Dyslipidemia_Diagnose_TC;
}

public String getDyslipidemia_Diagnose_TC(){
return this.Dyslipidemia_Diagnose_TC;
}

public void setWeight(double Weight){
this.Weight = Weight;
}

public double getWeight(){
return this.Weight;
}

public void setCr_Variable(double Cr_Variable){
this.Cr_Variable = Cr_Variable;
}

public double getCr_Variable(){
return this.Cr_Variable;
}

public void setACr_Variable(double ACr_Variable){
this.ACr_Variable = ACr_Variable;
}

public double getACr_Variable(){
return this.ACr_Variable;
}

public void setUrineProtein(double UrineProtein){
this.UrineProtein = UrineProtein;
}

public double getUrineProtein(){
return this.UrineProtein;
}

public void setDM_History(String DM_History){
this.DM_History = DM_History;
}

public String getDM_History(){
return this.DM_History;
}

public void setDM_Diagnose(String DM_Diagnose){
this.DM_Diagnose = DM_Diagnose;
}

public String getDM_Diagnose(){
return this.DM_Diagnose;
}

public void setHUA_Diagnose(String HUA_Diagnose){
this.HUA_Diagnose = HUA_Diagnose;
}

public String getHUA_Diagnose(){
return this.HUA_Diagnose;
}

public void setHypertension_Diagnose(String Hypertension_Diagnose){
this.Hypertension_Diagnose = Hypertension_Diagnose;
}

public String getHypertension_Diagnose(){
return this.Hypertension_Diagnose;
}

public void setNut(String Nut){
this.Nut = Nut;
}

public String getNut(){
return this.Nut;
}

public void setDietaryType(String DietaryType){
this.DietaryType = DietaryType;
}

public String getDietaryType(){
return this.DietaryType;
}

public void setCcr(double Ccr){
this.Ccr = Ccr;
}

public double getCcr(){
return this.Ccr;
}

public void setBaseProteinAmount(double BaseProteinAmount){
this.BaseProteinAmount = BaseProteinAmount;
}

public double getBaseProteinAmount(){
return this.BaseProteinAmount;
}

public void setProteinAmount_Temp(double ProteinAmount_Temp){
this.ProteinAmount_Temp = ProteinAmount_Temp;
}

public double getProteinAmount_Temp(){
return this.ProteinAmount_Temp;
}

public void setProteinRatio_Temp(double ProteinRatio_Temp){
this.ProteinRatio_Temp = ProteinRatio_Temp;
}

public double getProteinRatio_Temp(){
return this.ProteinRatio_Temp;
}

public void setProteinRatio(double ProteinRatio){
this.ProteinRatio = ProteinRatio;
}

public double getProteinRatio(){
return this.ProteinRatio;
}

public void setProteinAmount(double ProteinAmount){
this.ProteinAmount = ProteinAmount;
}

public double getProteinAmount(){
return this.ProteinAmount;
}

public void setCarboRatio(double CarboRatio){
this.CarboRatio = CarboRatio;
}

public double getCarboRatio(){
return this.CarboRatio;
}

public void setCarboAmount(double CarboAmount){
this.CarboAmount = CarboAmount;
}

public double getCarboAmount(){
return this.CarboAmount;
}

public void setFatRatio(double FatRatio){
this.FatRatio = FatRatio;
}

public double getFatRatio(){
return this.FatRatio;
}

public void setFatAmount(double FatAmount){
this.FatAmount = FatAmount;
}

public double getFatAmount(){
return this.FatAmount;
}

public void setMeatAmount(double MeatAmount){
this.MeatAmount = MeatAmount;
}

public double getMeatAmount(){
return this.MeatAmount;
}

public void setMilkAmount(double MilkAmount){
this.MilkAmount = MilkAmount;
}

public double getMilkAmount(){
return this.MilkAmount;
}

public void setEggAmount(double EggAmount){
this.EggAmount = EggAmount;
}

public double getEggAmount(){
return this.EggAmount;
}

public void setMainFood(double MainFood){
this.MainFood = MainFood;
}

public double getMainFood(){
return this.MainFood;
}

public void setFruit(double Fruit){
this.Fruit = Fruit;
}

public double getFruit(){
return this.Fruit;
}

public void setVegetable(double Vegetable){
this.Vegetable = Vegetable;
}

public double getVegetable(){
return this.Vegetable;
}

public void setTotalCarbo(double TotalCarbo){
this.TotalCarbo = TotalCarbo;
}

public double getTotalCarbo(){
return this.TotalCarbo;
}

public void setMeat(double Meat){
this.Meat = Meat;
}

public double getMeat(){
return this.Meat;
}

public void setTotalProtein(double TotalProtein){
this.TotalProtein = TotalProtein;
}

public double getTotalProtein(){
return this.TotalProtein;
}

public void setTotalFat(double TotalFat){
this.TotalFat = TotalFat;
}

public double getTotalFat(){
return this.TotalFat;
}

public void setOil(double Oil){
this.Oil = Oil;
}

public double getOil(){
return this.Oil;
}

public void setFat_Diagnose(String Fat_Diagnose){
this.Fat_Diagnose = Fat_Diagnose;
}

public String getFat_Diagnose(){
return this.Fat_Diagnose;
}

public void setMaxWater(double MaxWater){
this.MaxWater = MaxWater;
}

public double getMaxWater(){
return this.MaxWater;
}

public void setMinWater(double MinWater){
this.MinWater = MinWater;
}

public double getMinWater(){
return this.MinWater;
}

public void setSalt(double Salt){
this.Salt = Salt;
}

public double getSalt(){
return this.Salt;
}

public void setT1DMHis(String T1DMHis){
this.T1DMHis = T1DMHis;
}

public String getT1DMHis(){
return this.T1DMHis;
}

public void setT2DMHis(String T2DMHis){
this.T2DMHis = T2DMHis;
}

public String getT2DMHis(){
return this.T2DMHis;
}

public void setHbA1c(double HbA1c){
this.HbA1c = HbA1c;
}

public double getHbA1c(){
return this.HbA1c;
}

public void setFBG_Variable(double FBG_Variable){
this.FBG_Variable = FBG_Variable;
}

public double getFBG_Variable(){
return this.FBG_Variable;
}

public void settwoHPBG_Variable(double twoHPBG_Variable){
this.twoHPBG_Variable = twoHPBG_Variable;
}

public double gettwoHPBG_Variable(){
return this.twoHPBG_Variable;
}

public void setFat_History(String Fat_History){
this.Fat_History = Fat_History;
}

public String getFat_History(){
return this.Fat_History;
}

public void setDM_Family_History(String DM_Family_History){
this.DM_Family_History = DM_Family_History;
}

public String getDM_Family_History(){
return this.DM_Family_History;
}

public void setGDM_History(String GDM_History){
this.GDM_History = GDM_History;
}

public String getGDM_History(){
return this.GDM_History;
}

public void setMacrosomia_History(String Macrosomia_History){
this.Macrosomia_History = Macrosomia_History;
}

public String getMacrosomia_History(){
return this.Macrosomia_History;
}

public void setICA(String ICA){
this.ICA = ICA;
}

public String getICA(){
return this.ICA;
}

public void setGAD65(String GAD65){
this.GAD65 = GAD65;
}

public String getGAD65(){
return this.GAD65;
}

public void setFBG_OGTT_Variable(double FBG_OGTT_Variable){
this.FBG_OGTT_Variable = FBG_OGTT_Variable;
}

public double getFBG_OGTT_Variable(){
return this.FBG_OGTT_Variable;
}

public void settwoHPBG_OGTT_Variable(double twoHPBG_OGTT_Variable){
this.twoHPBG_OGTT_Variable = twoHPBG_OGTT_Variable;
}

public double gettwoHPBG_OGTT_Variable(){
return this.twoHPBG_OGTT_Variable;
}

public void setstatins_Drug(String statins_Drug){
this.statins_Drug = statins_Drug;
}

public String getstatins_Drug(){
return this.statins_Drug;
}

public void setLDLch_Reach_Standard(String LDLch_Reach_Standard){
this.LDLch_Reach_Standard = LDLch_Reach_Standard;
}

public String getLDLch_Reach_Standard(){
return this.LDLch_Reach_Standard;
}

public void setLDLch_First_Drug(String LDLch_First_Drug){
this.LDLch_First_Drug = LDLch_First_Drug;
}

public String getLDLch_First_Drug(){
return this.LDLch_First_Drug;
}

public void setrisk_score(double risk_score){
this.risk_score = risk_score;
}

public double getrisk_score(){
return this.risk_score;
}

public void setLDLch_Variable(double LDLch_Variable){
this.LDLch_Variable = LDLch_Variable;
}

public double getLDLch_Variable(){
return this.LDLch_Variable;
}

public void setTC_Variable(double TC_Variable){
this.TC_Variable = TC_Variable;
}

public double getTC_Variable(){
return this.TC_Variable;
}

public void setHDLch_Variable(double HDLch_Variable){
this.HDLch_Variable = HDLch_Variable;
}

public double getHDLch_Variable(){
return this.HDLch_Variable;
}

public void setDyslipidemia_Drug(String Dyslipidemia_Drug){
this.Dyslipidemia_Drug = Dyslipidemia_Drug;
}

public String getDyslipidemia_Drug(){
return this.Dyslipidemia_Drug;
}

public void setHDLch_First_Drug(String HDLch_First_Drug){
this.HDLch_First_Drug = HDLch_First_Drug;
}

public String getHDLch_First_Drug(){
return this.HDLch_First_Drug;
}

public void setHDLch_Reach_Standard(String HDLch_Reach_Standard){
this.HDLch_Reach_Standard = HDLch_Reach_Standard;
}

public String getHDLch_Reach_Standard(){
return this.HDLch_Reach_Standard;
}

public void setfibrates_Drug(String fibrates_Drug){
this.fibrates_Drug = fibrates_Drug;
}

public String getfibrates_Drug(){
return this.fibrates_Drug;
}

public void setTG_Variable(double TG_Variable){
this.TG_Variable = TG_Variable;
}

public double getTG_Variable(){
return this.TG_Variable;
}

public void setTG_First_Drug(String TG_First_Drug){
this.TG_First_Drug = TG_First_Drug;
}

public String getTG_First_Drug(){
return this.TG_First_Drug;
}

public void setTG_Reach_Standard(String TG_Reach_Standard){
this.TG_Reach_Standard = TG_Reach_Standard;
}

public String getTG_Reach_Standard(){
return this.TG_Reach_Standard;
}

public void setDyslipidemia_Diagnose_HDLC(String Dyslipidemia_Diagnose_HDLC){
this.Dyslipidemia_Diagnose_HDLC = Dyslipidemia_Diagnose_HDLC;
}

public String getDyslipidemia_Diagnose_HDLC(){
return this.Dyslipidemia_Diagnose_HDLC;
}

public void setDyslipidemia_Diagnose_LDLC(String Dyslipidemia_Diagnose_LDLC){
this.Dyslipidemia_Diagnose_LDLC = Dyslipidemia_Diagnose_LDLC;
}

public String getDyslipidemia_Diagnose_LDLC(){
return this.Dyslipidemia_Diagnose_LDLC;
}

public void setDyslipidemia_Diagnosed(String Dyslipidemia_Diagnosed){
this.Dyslipidemia_Diagnosed = Dyslipidemia_Diagnosed;
}

public String getDyslipidemia_Diagnosed(){
return this.Dyslipidemia_Diagnosed;
}

public void setDyslipidemia_History(String Dyslipidemia_History){
this.Dyslipidemia_History = Dyslipidemia_History;
}

public String getDyslipidemia_History(){
return this.Dyslipidemia_History;
}

public void setDyslipidemia_TG_His(String Dyslipidemia_TG_His){
this.Dyslipidemia_TG_His = Dyslipidemia_TG_His;
}

public String getDyslipidemia_TG_His(){
return this.Dyslipidemia_TG_His;
}

public void setDyslipidemia_TC_His(String Dyslipidemia_TC_His){
this.Dyslipidemia_TC_His = Dyslipidemia_TC_His;
}

public String getDyslipidemia_TC_His(){
return this.Dyslipidemia_TC_His;
}

public void setDyslipidemia_HDLch_His(String Dyslipidemia_HDLch_His){
this.Dyslipidemia_HDLch_His = Dyslipidemia_HDLch_His;
}

public String getDyslipidemia_HDLch_His(){
return this.Dyslipidemia_HDLch_His;
}

public void setDyslipidemia_LDLch_His(String Dyslipidemia_LDLch_His){
this.Dyslipidemia_LDLch_His = Dyslipidemia_LDLch_His;
}

public String getDyslipidemia_LDLch_His(){
return this.Dyslipidemia_LDLch_His;
}

public void setwaistline_Variable(double waistline_Variable){
this.waistline_Variable = waistline_Variable;
}

public double getwaistline_Variable(){
return this.waistline_Variable;
}

public void setAcute_Gouty_Arthritis_History(String Acute_Gouty_Arthritis_History){
this.Acute_Gouty_Arthritis_History = Acute_Gouty_Arthritis_History;
}

public String getAcute_Gouty_Arthritis_History(){
return this.Acute_Gouty_Arthritis_History;
}

public void setHyperuricaemia_History(String Hyperuricaemia_History){
this.Hyperuricaemia_History = Hyperuricaemia_History;
}

public String getHyperuricaemia_History(){
return this.Hyperuricaemia_History;
}

public void setarthritis_flare(String arthritis_flare){
this.arthritis_flare = arthritis_flare;
}

public String getarthritis_flare(){
return this.arthritis_flare;
}

public void setHUA_Diagnose_Acute(String HUA_Diagnose_Acute){
this.HUA_Diagnose_Acute = HUA_Diagnose_Acute;
}

public String getHUA_Diagnose_Acute(){
return this.HUA_Diagnose_Acute;
}

public void setUA_Variable(double UA_Variable){
this.UA_Variable = UA_Variable;
}

public double getUA_Variable(){
return this.UA_Variable;
}

public void setHUA_Diagnose_PS(String HUA_Diagnose_PS){
this.HUA_Diagnose_PS = HUA_Diagnose_PS;
}

public String getHUA_Diagnose_PS(){
return this.HUA_Diagnose_PS;
}

public void setUA_Down_drug(String UA_Down_drug){
this.UA_Down_drug = UA_Down_drug;
}

public String getUA_Down_drug(){
return this.UA_Down_drug;
}

public void setAcute_Gouty_Arthritis_Period(String Acute_Gouty_Arthritis_Period){
this.Acute_Gouty_Arthritis_Period = Acute_Gouty_Arthritis_Period;
}

public String getAcute_Gouty_Arthritis_Period(){
return this.Acute_Gouty_Arthritis_Period;
}

public void setUUA(double UUA){
this.UUA = UUA;
}

public double getUUA(){
return this.UUA;
}

public void setabnormal_renal_function(String abnormal_renal_function){
this.abnormal_renal_function = abnormal_renal_function;
}

public String getabnormal_renal_function(){
return this.abnormal_renal_function;
}

public void setGout_History(String Gout_History){
this.Gout_History = Gout_History;
}

public String getGout_History(){
return this.Gout_History;
}

public void setHUA_Diagnose_Gouty(String HUA_Diagnose_Gouty){
this.HUA_Diagnose_Gouty = HUA_Diagnose_Gouty;
}

public String getHUA_Diagnose_Gouty(){
return this.HUA_Diagnose_Gouty;
}

public void setUPh(double UPh){
this.UPh = UPh;
}

public double getUPh(){
return this.UPh;
}

public void setMalignant_Tumour(String Malignant_Tumour){
this.Malignant_Tumour = Malignant_Tumour;
}

public String getMalignant_Tumour(){
return this.Malignant_Tumour;
}

public void setChemotherapy(String Chemotherapy){
this.Chemotherapy = Chemotherapy;
}

public String getChemotherapy(){
return this.Chemotherapy;
}

public void setNephropathy(String Nephropathy){
this.Nephropathy = Nephropathy;
}

public String getNephropathy(){
return this.Nephropathy;
}

public void setDose_Affect_UA_Excretion(String Dose_Affect_UA_Excretion){
this.Dose_Affect_UA_Excretion = Dose_Affect_UA_Excretion;
}

public String getDose_Affect_UA_Excretion(){
return this.Dose_Affect_UA_Excretion;
}

public void setCerebrovascular_Disease_History(String Cerebrovascular_Disease_History){
this.Cerebrovascular_Disease_History = Cerebrovascular_Disease_History;
}

public String getCerebrovascular_Disease_History(){
return this.Cerebrovascular_Disease_History;
}

public void setSBP_Current_Variable(double SBP_Current_Variable){
this.SBP_Current_Variable = SBP_Current_Variable;
}

public double getSBP_Current_Variable(){
return this.SBP_Current_Variable;
}

public void setDBP_Current_Variable(double DBP_Current_Variable){
this.DBP_Current_Variable = DBP_Current_Variable;
}

public double getDBP_Current_Variable(){
return this.DBP_Current_Variable;
}

public void setHT_Down_drug(String HT_Down_drug){
this.HT_Down_drug = HT_Down_drug;
}

public String getHT_Down_drug(){
return this.HT_Down_drug;
}

public void sethypertension_Diagnose_Stage(String hypertension_Diagnose_Stage){
this.hypertension_Diagnose_Stage = hypertension_Diagnose_Stage;
}

public String gethypertension_Diagnose_Stage(){
return this.hypertension_Diagnose_Stage;
}

public void setheart_rate(double heart_rate){
this.heart_rate = heart_rate;
}

public double getheart_rate(){
return this.heart_rate;
}

public void setirenal_artery_Bistenosis(String irenal_artery_Bistenosis){
this.irenal_artery_Bistenosis = irenal_artery_Bistenosis;
}

public String getirenal_artery_Bistenosis(){
return this.irenal_artery_Bistenosis;
}

public void setDM_kidney(String DM_kidney){
this.DM_kidney = DM_kidney;
}

public String getDM_kidney(){
return this.DM_kidney;
}

public void setrenal_artery_stenosis(String renal_artery_stenosis){
this.renal_artery_stenosis = renal_artery_stenosis;
}

public String getrenal_artery_stenosis(){
return this.renal_artery_stenosis;
}

public void setHypertension_Diagnose_PS(String Hypertension_Diagnose_PS){
this.Hypertension_Diagnose_PS = Hypertension_Diagnose_PS;
}

public String getHypertension_Diagnose_PS(){
return this.Hypertension_Diagnose_PS;
}

public void setDBP_Top_Variable(double DBP_Top_Variable){
this.DBP_Top_Variable = DBP_Top_Variable;
}

public double getDBP_Top_Variable(){
return this.DBP_Top_Variable;
}

public void setSBP_Top_Variable(double SBP_Top_Variable){
this.SBP_Top_Variable = SBP_Top_Variable;
}

public double getSBP_Top_Variable(){
return this.SBP_Top_Variable;
}

public void setCardiopathy_History(String Cardiopathy_History){
this.Cardiopathy_History = Cardiopathy_History;
}

public String getCardiopathy_History(){
return this.Cardiopathy_History;
}

public void setPeripheral_Vascular_Disease_History(String Peripheral_Vascular_Disease_History){
this.Peripheral_Vascular_Disease_History = Peripheral_Vascular_Disease_History;
}

public String getPeripheral_Vascular_Disease_History(){
return this.Peripheral_Vascular_Disease_History;
}

public void setRetinopathy_History(String Retinopathy_History){
this.Retinopathy_History = Retinopathy_History;
}

public String getRetinopathy_History(){
return this.Retinopathy_History;
}

public void setHyperuricaemia_Diagnose_risklevel(String Hyperuricaemia_Diagnose_risklevel){
this.Hyperuricaemia_Diagnose_risklevel = Hyperuricaemia_Diagnose_risklevel;
}

public String getHyperuricaemia_Diagnose_risklevel(){
return this.Hyperuricaemia_Diagnose_risklevel;
}

public void setsmoke_history(String smoke_history){
this.smoke_history = smoke_history;
}

public String getsmoke_history(){
return this.smoke_history;
}

public void setCardiovascular_Disease_Family_History(String Cardiovascular_Disease_Family_History){
this.Cardiovascular_Disease_Family_History = Cardiovascular_Disease_Family_History;
}

public String getCardiovascular_Disease_Family_History(){
return this.Cardiovascular_Disease_Family_History;
}

public void setlack_of_exercise(String lack_of_exercise){
this.lack_of_exercise = lack_of_exercise;
}

public String getlack_of_exercise(){
return this.lack_of_exercise;
}

public void setHypertension_History(String Hypertension_History){
this.Hypertension_History = Hypertension_History;
}

public String getHypertension_History(){
return this.Hypertension_History;
}

public void setMetabolic_Syndrome_Conclude(String Metabolic_Syndrome_Conclude){
this.Metabolic_Syndrome_Conclude = Metabolic_Syndrome_Conclude;
}

public String getMetabolic_Syndrome_Conclude(){
return this.Metabolic_Syndrome_Conclude;
}

public void setHypertension_Family_History(String Hypertension_Family_History){
this.Hypertension_Family_History = Hypertension_Family_History;
}

public String getHypertension_Family_History(){
return this.Hypertension_Family_History;
}

public void setDyslipidemia_Family_History(String Dyslipidemia_Family_History){
this.Dyslipidemia_Family_History = Dyslipidemia_Family_History;
}

public String getDyslipidemia_Family_History(){
return this.Dyslipidemia_Family_History;
}

public void setHyperuricemia_Family_History(String Hyperuricemia_Family_History){
this.Hyperuricemia_Family_History = Hyperuricemia_Family_History;
}

public String getHyperuricemia_Family_History(){
return this.Hyperuricemia_Family_History;
}

public void setCoronary_Heart_Disease_Family_History(String Coronary_Heart_Disease_Family_History){
this.Coronary_Heart_Disease_Family_History = Coronary_Heart_Disease_Family_History;
}

public String getCoronary_Heart_Disease_Family_History(){
return this.Coronary_Heart_Disease_Family_History;
}

public void setCerebral_Infarct_Family_History(String Cerebral_Infarct_Family_History){
this.Cerebral_Infarct_Family_History = Cerebral_Infarct_Family_History;
}

public String getCerebral_Infarct_Family_History(){
return this.Cerebral_Infarct_Family_History;
}

public void setCerebral_Infarct(String Cerebral_Infarct){
this.Cerebral_Infarct = Cerebral_Infarct;
}

public String getCerebral_Infarct(){
return this.Cerebral_Infarct;
}

public void setLower_Extremity_Angiopathy(String Lower_Extremity_Angiopathy){
this.Lower_Extremity_Angiopathy = Lower_Extremity_Angiopathy;
}

public String getLower_Extremity_Angiopathy(){
return this.Lower_Extremity_Angiopathy;
}

public void setMSRiskDegree(String MSRiskDegree){
this.MSRiskDegree = MSRiskDegree;
}

public String getMSRiskDegree(){
return this.MSRiskDegree;
}

public void setIFGHis(String IFGHis){
this.IFGHis = IFGHis;
}

public String getIFGHis(){
return this.IFGHis;
}

public void setIGTHis(String IGTHis){
this.IGTHis = IGTHis;
}

public String getIGTHis(){
return this.IGTHis;
}

public void setIGRHis(String IGRHis){
this.IGRHis = IGRHis;
}

public String getIGRHis(){
return this.IGRHis;
}

public void setDM_Drug(String DM_Drug){
this.DM_Drug = DM_Drug;
}

public String getDM_Drug(){
return this.DM_Drug;
}

public void setInsolin(String Insolin){
this.Insolin = Insolin;
}

public String getInsolin(){
return this.Insolin;
}

public void setShuanggua_Drug(String Shuanggua_Drug){
this.Shuanggua_Drug = Shuanggua_Drug;
}

public String getShuanggua_Drug(){
return this.Shuanggua_Drug;
}

public void setGelienai_Drug(String Gelienai_Drug){
this.Gelienai_Drug = Gelienai_Drug;
}

public String getGelienai_Drug(){
return this.Gelienai_Drug;
}

public void setGelietong_Drug(String Gelietong_Drug){
this.Gelietong_Drug = Gelietong_Drug;
}

public String getGelietong_Drug(){
return this.Gelietong_Drug;
}

public void setHuangniao_Drug(String Huangniao_Drug){
this.Huangniao_Drug = Huangniao_Drug;
}

public String getHuangniao_Drug(){
return this.Huangniao_Drug;
}

public void setAGI_Drug(String AGI_Drug){
this.AGI_Drug = AGI_Drug;
}

public String getAGI_Drug(){
return this.AGI_Drug;
}

public void setTC_Reach_Standard(String TC_Reach_Standard){
this.TC_Reach_Standard = TC_Reach_Standard;
}

public String getTC_Reach_Standard(){
return this.TC_Reach_Standard;
}

public void setTC_First_Drug(String TC_First_Drug){
this.TC_First_Drug = TC_First_Drug;
}

public String getTC_First_Drug(){
return this.TC_First_Drug;
}

public void setGlucoseLevel(String GlucoseLevel){
this.GlucoseLevel = GlucoseLevel;
}

public String getGlucoseLevel(){
return this.GlucoseLevel;
}

public void setGLByFBGA(String GLByFBGA){
this.GLByFBGA = GLByFBGA;
}

public String getGLByFBGA(){
return this.GLByFBGA;
}

public void setGLByRBGA(String GLByRBGA){
this.GLByRBGA = GLByRBGA;
}

public String getGLByRBGA(){
return this.GLByRBGA;
}

public void setBG_Variable(double BG_Variable){
this.BG_Variable = BG_Variable;
}

public double getBG_Variable(){
return this.BG_Variable;
}

public void setReduceWeight(String ReduceWeight){
this.ReduceWeight = ReduceWeight;
}

public String getReduceWeight(){
return this.ReduceWeight;
}

public void setReduceBG(String ReduceBG){
this.ReduceBG = ReduceBG;
}

public String getReduceBG(){
return this.ReduceBG;
}

public void setStrengthenPhysique(String StrengthenPhysique){
this.StrengthenPhysique = StrengthenPhysique;
}

public String getStrengthenPhysique(){
return this.StrengthenPhysique;
}

public void setReduceBGCal(double ReduceBGCal){
this.ReduceBGCal = ReduceBGCal;
}

public double getReduceBGCal(){
return this.ReduceBGCal;
}

public void setReduceWeightCal(double ReduceWeightCal){
this.ReduceWeightCal = ReduceWeightCal;
}

public double getReduceWeightCal(){
return this.ReduceWeightCal;
}

public void setLimbDyskinesia(String LimbDyskinesia){
this.LimbDyskinesia = LimbDyskinesia;
}

public String getLimbDyskinesia(){
return this.LimbDyskinesia;
}

public void setSportTypeLow(String SportTypeLow){
this.SportTypeLow = SportTypeLow;
}

public String getSportTypeLow(){
return this.SportTypeLow;
}

public void setSportTypeMiddle(String SportTypeMiddle){
this.SportTypeMiddle = SportTypeMiddle;
}

public String getSportTypeMiddle(){
return this.SportTypeMiddle;
}

public void setSportTypeHigh(String SportTypeHigh){
this.SportTypeHigh = SportTypeHigh;
}

public String getSportTypeHigh(){
return this.SportTypeHigh;
}

public void setLEnergyConsumption(double LEnergyConsumption){
this.LEnergyConsumption = LEnergyConsumption;
}

public double getLEnergyConsumption(){
return this.LEnergyConsumption;
}

public void setMEnergyConsumption(double MEnergyConsumption){
this.MEnergyConsumption = MEnergyConsumption;
}

public double getMEnergyConsumption(){
return this.MEnergyConsumption;
}

public void setHEnergyConsumption(double HEnergyConsumption){
this.HEnergyConsumption = HEnergyConsumption;
}

public double getHEnergyConsumption(){
return this.HEnergyConsumption;
}
}