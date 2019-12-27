# 创建patient类
# 包括成员变量及相应成员方法

import json

r = open('entrance_variable_class.txt', 'r')
dict_new = r.read()
r.close()
member_var_new = json.loads(dict_new)
f = open('patient.java', 'w')
patient = ''
patient += 'package com.sample;\n\npublic class Patient {\n\n'
for name in member_var_new:
    patient += 'public %s %s;\n' % (member_var_new[name], name)
for name in member_var_new:
    patient += '\n'
    patient += 'public void set%s(%s %s){\n' % (name, member_var_new[name], name)
    patient += 'this.%s = %s;\n' % (name, name)
    patient += '}\n\n'
    patient += 'public %s get%s(){\n' % (member_var_new[name], name)
    patient += 'return this.%s;\n' % (name)
    patient += '}\n'
patient += '}'
f.write(patient)
f.close()

# #修改成员变量数据类型
# r = open('variable_new3.txt','r')
# dict_new = r.read()
# r.close()
# member_var_new = json.loads(dict_new)
# f = open('variable_new2.txt','r')
# dict = f.read()
# f.close()
# member_var = json.loads(dict)
# for var_name in  member_var_new:
#     if var_name in member_var:
#         member_var_new[var_name] = member_var[var_name]
# r = open('variable_new3.txt','w')
# en_json = json.dumps(member_var_new)
# r.write(en_json)
# r.close()


# double_var = ['BMI','Height','Age','SportLevel','IdealBMI','SexCoeff','AgeCoeff',
#               'DiseaseStatusCoeff','Weight','Cr_Variable','ACr_Variable','TKcal',
#               'UrineProtein','MilkAmount','EggAmount','Ccr','HbA1c','FBG_Variable',
#               'twoHPBG_Variable','FBG_OGTT_Variable','twoHPBG_OGTT_Variable','risk_score',
#               'LDLch_Variable','TC_Variable','HDLch_Variable','TG_Variable','waistline_Variable',
#               'UA_Variable','UUA','UPh','SBP_Current_Variable','DBP_Current_Variable','heart_rate',
#               'DBP_Top_Variable','SBP_Top_Variable','BG_Variable','ReduceBGCal','ReduceWeightCal',
#               'LEnergyConsumption','MEnergyConsumption','HEnergyConsumption']
