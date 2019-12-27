# Generated from E:/pycharm/repository/lex\clipsparser.g4 by ANTLR 4.7.2
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .clipsparser import clipsparser
else:
    from clipsparser import clipsparser


# This class defines a complete listener for a parse tree produced by clipsparser.
class clipsparserListener(ParseTreeListener):

    # Enter a parse tree produced by clipsparser#prog.
    def enterProg(self, ctx: clipsparser.ProgContext):
        pass

    # Exit a parse tree produced by clipsparser#prog.
    def exitProg(self, ctx: clipsparser.ProgContext):
        pass

    # Enter a parse tree produced by clipsparser#variable.
    def enterVariable(self, ctx: clipsparser.VariableContext):
        pass

    # Exit a parse tree produced by clipsparser#variable.
    def exitVariable(self, ctx: clipsparser.VariableContext):
        pass

    # Enter a parse tree produced by clipsparser#Expression_constant.
    def enterExpression_constant(self, ctx: clipsparser.Expression_constantContext):
        pass

    # Exit a parse tree produced by clipsparser#Expression_constant.
    def exitExpression_constant(self, ctx: clipsparser.Expression_constantContext):
        pass

    # Enter a parse tree produced by clipsparser#Expression_variable.
    def enterExpression_variable(self, ctx: clipsparser.Expression_variableContext):
        pass

    # Exit a parse tree produced by clipsparser#Expression_variable.
    def exitExpression_variable(self, ctx: clipsparser.Expression_variableContext):
        pass

    # Enter a parse tree produced by clipsparser#Expression_functioncall.
    def enterExpression_functioncall(self, ctx: clipsparser.Expression_functioncallContext):
        pass

    # Exit a parse tree produced by clipsparser#Expression_functioncall.
    def exitExpression_functioncall(self, ctx: clipsparser.Expression_functioncallContext):
        pass

    # Enter a parse tree produced by clipsparser#Expression_conditionalelement.
    def enterExpression_conditionalelement(self, ctx: clipsparser.Expression_conditionalelementContext):
        pass

    # Exit a parse tree produced by clipsparser#Expression_conditionalelement.
    def exitExpression_conditionalelement(self, ctx: clipsparser.Expression_conditionalelementContext):
        pass

    # Enter a parse tree produced by clipsparser#Expression_mathname.
    def enterExpression_mathname(self, ctx: clipsparser.Expression_mathnameContext):
        pass

    # Exit a parse tree produced by clipsparser#Expression_mathname.
    def exitExpression_mathname(self, ctx: clipsparser.Expression_mathnameContext):
        pass

    # Enter a parse tree produced by clipsparser#Expression_predicate_name.
    def enterExpression_predicate_name(self, ctx: clipsparser.Expression_predicate_nameContext):
        pass

    # Exit a parse tree produced by clipsparser#Expression_predicate_name.
    def exitExpression_predicate_name(self, ctx: clipsparser.Expression_predicate_nameContext):
        pass

    # Enter a parse tree produced by clipsparser#Expression_COMMENT.
    def enterExpression_COMMENT(self, ctx: clipsparser.Expression_COMMENTContext):
        pass

    # Exit a parse tree produced by clipsparser#Expression_COMMENT.
    def exitExpression_COMMENT(self, ctx: clipsparser.Expression_COMMENTContext):
        pass

    # Enter a parse tree produced by clipsparser#action.
    def enterAction(self, ctx: clipsparser.ActionContext):
        pass

    # Exit a parse tree produced by clipsparser#action.
    def exitAction(self, ctx: clipsparser.ActionContext):
        pass

    # Enter a parse tree produced by clipsparser#construct.
    def enterConstruct(self, ctx: clipsparser.ConstructContext):
        pass

    # Exit a parse tree produced by clipsparser#construct.
    def exitConstruct(self, ctx: clipsparser.ConstructContext):
        pass

    # Enter a parse tree produced by clipsparser#numeric_expression.
    def enterNumeric_expression(self, ctx: clipsparser.Numeric_expressionContext):
        pass

    # Exit a parse tree produced by clipsparser#numeric_expression.
    def exitNumeric_expression(self, ctx: clipsparser.Numeric_expressionContext):
        pass

    # Enter a parse tree produced by clipsparser#singlefield_expression.
    def enterSinglefield_expression(self, ctx: clipsparser.Singlefield_expressionContext):
        pass

    # Exit a parse tree produced by clipsparser#singlefield_expression.
    def exitSinglefield_expression(self, ctx: clipsparser.Singlefield_expressionContext):
        pass

    # Enter a parse tree produced by clipsparser#multifield_expression.
    def enterMultifield_expression(self, ctx: clipsparser.Multifield_expressionContext):
        pass

    # Exit a parse tree produced by clipsparser#multifield_expression.
    def exitMultifield_expression(self, ctx: clipsparser.Multifield_expressionContext):
        pass

    # Enter a parse tree produced by clipsparser#test_expression.
    def enterTest_expression(self, ctx: clipsparser.Test_expressionContext):
        pass

    # Exit a parse tree produced by clipsparser#test_expression.
    def exitTest_expression(self, ctx: clipsparser.Test_expressionContext):
        pass

    # Enter a parse tree produced by clipsparser#comparison_expression.
    def enterComparison_expression(self, ctx: clipsparser.Comparison_expressionContext):
        pass

    # Exit a parse tree produced by clipsparser#comparison_expression.
    def exitComparison_expression(self, ctx: clipsparser.Comparison_expressionContext):
        pass

    # Enter a parse tree produced by clipsparser#lexeme_expression.
    def enterLexeme_expression(self, ctx: clipsparser.Lexeme_expressionContext):
        pass

    # Exit a parse tree produced by clipsparser#lexeme_expression.
    def exitLexeme_expression(self, ctx: clipsparser.Lexeme_expressionContext):
        pass

    # Enter a parse tree produced by clipsparser#predicate_name.
    def enterPredicate_name(self, ctx: clipsparser.Predicate_nameContext):
        pass

    # Exit a parse tree produced by clipsparser#predicate_name.
    def exitPredicate_name(self, ctx: clipsparser.Predicate_nameContext):
        pass

    # Enter a parse tree produced by clipsparser#connected_name.
    def enterConnected_name(self, ctx: clipsparser.Connected_nameContext):
        pass

    # Exit a parse tree produced by clipsparser#connected_name.
    def exitConnected_name(self, ctx: clipsparser.Connected_nameContext):
        pass

    # Enter a parse tree produced by clipsparser#math_name.
    def enterMath_name(self, ctx: clipsparser.Math_nameContext):
        pass

    # Exit a parse tree produced by clipsparser#math_name.
    def exitMath_name(self, ctx: clipsparser.Math_nameContext):
        pass

    # Enter a parse tree produced by clipsparser#function_name.
    def enterFunction_name(self, ctx: clipsparser.Function_nameContext):
        pass

    # Exit a parse tree produced by clipsparser#function_name.
    def exitFunction_name(self, ctx: clipsparser.Function_nameContext):
        pass

    # Enter a parse tree produced by clipsparser#function_call.
    def enterFunction_call(self, ctx: clipsparser.Function_callContext):
        pass

    # Exit a parse tree produced by clipsparser#function_call.
    def exitFunction_call(self, ctx: clipsparser.Function_callContext):
        pass

    # Enter a parse tree produced by clipsparser#tradition_function.
    def enterTradition_function(self, ctx: clipsparser.Tradition_functionContext):
        pass

    # Exit a parse tree produced by clipsparser#tradition_function.
    def exitTradition_function(self, ctx: clipsparser.Tradition_functionContext):
        pass

    # Enter a parse tree produced by clipsparser#math_function.
    def enterMath_function(self, ctx: clipsparser.Math_functionContext):
        pass

    # Exit a parse tree produced by clipsparser#math_function.
    def exitMath_function(self, ctx: clipsparser.Math_functionContext):
        pass

    # Enter a parse tree produced by clipsparser#predicate_function.
    def enterPredicate_function(self, ctx: clipsparser.Predicate_functionContext):
        pass

    # Exit a parse tree produced by clipsparser#predicate_function.
    def exitPredicate_function(self, ctx: clipsparser.Predicate_functionContext):
        pass

    # Enter a parse tree produced by clipsparser#connected_function.
    def enterConnected_function(self, ctx: clipsparser.Connected_functionContext):
        pass

    # Exit a parse tree produced by clipsparser#connected_function.
    def exitConnected_function(self, ctx: clipsparser.Connected_functionContext):
        pass

    # Enter a parse tree produced by clipsparser#procedural_function.
    def enterProcedural_function(self, ctx: clipsparser.Procedural_functionContext):
        pass

    # Exit a parse tree produced by clipsparser#procedural_function.
    def exitProcedural_function(self, ctx: clipsparser.Procedural_functionContext):
        pass

    # Enter a parse tree produced by clipsparser#if_then_else.
    def enterIf_then_else(self, ctx: clipsparser.If_then_elseContext):
        pass

    # Exit a parse tree produced by clipsparser#if_then_else.
    def exitIf_then_else(self, ctx: clipsparser.If_then_elseContext):
        pass

    # Enter a parse tree produced by clipsparser#while_do.
    def enterWhile_do(self, ctx: clipsparser.While_doContext):
        pass

    # Exit a parse tree produced by clipsparser#while_do.
    def exitWhile_do(self, ctx: clipsparser.While_doContext):
        pass

    # Enter a parse tree produced by clipsparser#switch_stmt.
    def enterSwitch_stmt(self, ctx: clipsparser.Switch_stmtContext):
        pass

    # Exit a parse tree produced by clipsparser#switch_stmt.
    def exitSwitch_stmt(self, ctx: clipsparser.Switch_stmtContext):
        pass

    # Enter a parse tree produced by clipsparser#foreach.
    def enterForeach(self, ctx: clipsparser.ForeachContext):
        pass

    # Exit a parse tree produced by clipsparser#foreach.
    def exitForeach(self, ctx: clipsparser.ForeachContext):
        pass

    # Enter a parse tree produced by clipsparser#loop_for_count.
    def enterLoop_for_count(self, ctx: clipsparser.Loop_for_countContext):
        pass

    # Exit a parse tree produced by clipsparser#loop_for_count.
    def exitLoop_for_count(self, ctx: clipsparser.Loop_for_countContext):
        pass

    # Enter a parse tree produced by clipsparser#return_stmt.
    def enterReturn_stmt(self, ctx: clipsparser.Return_stmtContext):
        pass

    # Exit a parse tree produced by clipsparser#return_stmt.
    def exitReturn_stmt(self, ctx: clipsparser.Return_stmtContext):
        pass

    # Enter a parse tree produced by clipsparser#break_stmt.
    def enterBreak_stmt(self, ctx: clipsparser.Break_stmtContext):
        pass

    # Exit a parse tree produced by clipsparser#break_stmt.
    def exitBreak_stmt(self, ctx: clipsparser.Break_stmtContext):
        pass

    # Enter a parse tree produced by clipsparser#case_stmt.
    def enterCase_stmt(self, ctx: clipsparser.Case_stmtContext):
        pass

    # Exit a parse tree produced by clipsparser#case_stmt.
    def exitCase_stmt(self, ctx: clipsparser.Case_stmtContext):
        pass

    # Enter a parse tree produced by clipsparser#default_stmt.
    def enterDefault_stmt(self, ctx: clipsparser.Default_stmtContext):
        pass

    # Exit a parse tree produced by clipsparser#default_stmt.
    def exitDefault_stmt(self, ctx: clipsparser.Default_stmtContext):
        pass

    # Enter a parse tree produced by clipsparser#range_spec.
    def enterRange_spec(self, ctx: clipsparser.Range_specContext):
        pass

    # Exit a parse tree produced by clipsparser#range_spec.
    def exitRange_spec(self, ctx: clipsparser.Range_specContext):
        pass

    # Enter a parse tree produced by clipsparser#deffacts.
    def enterDeffacts(self, ctx: clipsparser.DeffactsContext):
        pass

    # Exit a parse tree produced by clipsparser#deffacts.
    def exitDeffacts(self, ctx: clipsparser.DeffactsContext):
        pass

    # Enter a parse tree produced by clipsparser#ordered_rhs_pattern.
    def enterOrdered_rhs_pattern(self, ctx: clipsparser.Ordered_rhs_patternContext):
        pass

    # Exit a parse tree produced by clipsparser#ordered_rhs_pattern.
    def exitOrdered_rhs_pattern(self, ctx: clipsparser.Ordered_rhs_patternContext):
        pass

    # Enter a parse tree produced by clipsparser#template_rhs_pattern.
    def enterTemplate_rhs_pattern(self, ctx: clipsparser.Template_rhs_patternContext):
        pass

    # Exit a parse tree produced by clipsparser#template_rhs_pattern.
    def exitTemplate_rhs_pattern(self, ctx: clipsparser.Template_rhs_patternContext):
        pass

    # Enter a parse tree produced by clipsparser#rhs_slot.
    def enterRhs_slot(self, ctx: clipsparser.Rhs_slotContext):
        pass

    # Exit a parse tree produced by clipsparser#rhs_slot.
    def exitRhs_slot(self, ctx: clipsparser.Rhs_slotContext):
        pass

    # Enter a parse tree produced by clipsparser#single_field_rhs_slot.
    def enterSingle_field_rhs_slot(self, ctx: clipsparser.Single_field_rhs_slotContext):
        pass

    # Exit a parse tree produced by clipsparser#single_field_rhs_slot.
    def exitSingle_field_rhs_slot(self, ctx: clipsparser.Single_field_rhs_slotContext):
        pass

    # Enter a parse tree produced by clipsparser#multi_field_rhs_slot.
    def enterMulti_field_rhs_slot(self, ctx: clipsparser.Multi_field_rhs_slotContext):
        pass

    # Exit a parse tree produced by clipsparser#multi_field_rhs_slot.
    def exitMulti_field_rhs_slot(self, ctx: clipsparser.Multi_field_rhs_slotContext):
        pass

    # Enter a parse tree produced by clipsparser#rhs_field.
    def enterRhs_field(self, ctx: clipsparser.Rhs_fieldContext):
        pass

    # Exit a parse tree produced by clipsparser#rhs_field.
    def exitRhs_field(self, ctx: clipsparser.Rhs_fieldContext):
        pass

    # Enter a parse tree produced by clipsparser#rhs_pattern.
    def enterRhs_pattern(self, ctx: clipsparser.Rhs_patternContext):
        pass

    # Exit a parse tree produced by clipsparser#rhs_pattern.
    def exitRhs_pattern(self, ctx: clipsparser.Rhs_patternContext):
        pass

    # Enter a parse tree produced by clipsparser#deftemplate.
    def enterDeftemplate(self, ctx: clipsparser.DeftemplateContext):
        pass

    # Exit a parse tree produced by clipsparser#deftemplate.
    def exitDeftemplate(self, ctx: clipsparser.DeftemplateContext):
        pass

    # Enter a parse tree produced by clipsparser#slot_definition.
    def enterSlot_definition(self, ctx: clipsparser.Slot_definitionContext):
        pass

    # Exit a parse tree produced by clipsparser#slot_definition.
    def exitSlot_definition(self, ctx: clipsparser.Slot_definitionContext):
        pass

    # Enter a parse tree produced by clipsparser#single_slot.
    def enterSingle_slot(self, ctx: clipsparser.Single_slotContext):
        pass

    # Exit a parse tree produced by clipsparser#single_slot.
    def exitSingle_slot(self, ctx: clipsparser.Single_slotContext):
        pass

    # Enter a parse tree produced by clipsparser#multi_slot.
    def enterMulti_slot(self, ctx: clipsparser.Multi_slotContext):
        pass

    # Exit a parse tree produced by clipsparser#multi_slot.
    def exitMulti_slot(self, ctx: clipsparser.Multi_slotContext):
        pass

    # Enter a parse tree produced by clipsparser#template_attr.
    def enterTemplate_attr(self, ctx: clipsparser.Template_attrContext):
        pass

    # Exit a parse tree produced by clipsparser#template_attr.
    def exitTemplate_attr(self, ctx: clipsparser.Template_attrContext):
        pass

    # Enter a parse tree produced by clipsparser#default_attr.
    def enterDefault_attr(self, ctx: clipsparser.Default_attrContext):
        pass

    # Exit a parse tree produced by clipsparser#default_attr.
    def exitDefault_attr(self, ctx: clipsparser.Default_attrContext):
        pass

    # Enter a parse tree produced by clipsparser#constaint_attr.
    def enterConstaint_attr(self, ctx: clipsparser.Constaint_attrContext):
        pass

    # Exit a parse tree produced by clipsparser#constaint_attr.
    def exitConstaint_attr(self, ctx: clipsparser.Constaint_attrContext):
        pass

    # Enter a parse tree produced by clipsparser#type_attr.
    def enterType_attr(self, ctx: clipsparser.Type_attrContext):
        pass

    # Exit a parse tree produced by clipsparser#type_attr.
    def exitType_attr(self, ctx: clipsparser.Type_attrContext):
        pass

    # Enter a parse tree produced by clipsparser#allowed_attr.
    def enterAllowed_attr(self, ctx: clipsparser.Allowed_attrContext):
        pass

    # Exit a parse tree produced by clipsparser#allowed_attr.
    def exitAllowed_attr(self, ctx: clipsparser.Allowed_attrContext):
        pass

    # Enter a parse tree produced by clipsparser#range_attr.
    def enterRange_attr(self, ctx: clipsparser.Range_attrContext):
        pass

    # Exit a parse tree produced by clipsparser#range_attr.
    def exitRange_attr(self, ctx: clipsparser.Range_attrContext):
        pass

    # Enter a parse tree produced by clipsparser#cardinality_attr.
    def enterCardinality_attr(self, ctx: clipsparser.Cardinality_attrContext):
        pass

    # Exit a parse tree produced by clipsparser#cardinality_attr.
    def exitCardinality_attr(self, ctx: clipsparser.Cardinality_attrContext):
        pass

    # Enter a parse tree produced by clipsparser#allowed_type.
    def enterAllowed_type(self, ctx: clipsparser.Allowed_typeContext):
        pass

    # Exit a parse tree produced by clipsparser#allowed_type.
    def exitAllowed_type(self, ctx: clipsparser.Allowed_typeContext):
        pass

    # Enter a parse tree produced by clipsparser#class_name.
    def enterClass_name(self, ctx: clipsparser.Class_nameContext):
        pass

    # Exit a parse tree produced by clipsparser#class_name.
    def exitClass_name(self, ctx: clipsparser.Class_nameContext):
        pass

    # Enter a parse tree produced by clipsparser#range_specification.
    def enterRange_specification(self, ctx: clipsparser.Range_specificationContext):
        pass

    # Exit a parse tree produced by clipsparser#range_specification.
    def exitRange_specification(self, ctx: clipsparser.Range_specificationContext):
        pass

    # Enter a parse tree produced by clipsparser#cardinality_specification.
    def enterCardinality_specification(self, ctx: clipsparser.Cardinality_specificationContext):
        pass

    # Exit a parse tree produced by clipsparser#cardinality_specification.
    def exitCardinality_specification(self, ctx: clipsparser.Cardinality_specificationContext):
        pass

    # Enter a parse tree produced by clipsparser#defglobal.
    def enterDefglobal(self, ctx: clipsparser.DefglobalContext):
        pass

    # Exit a parse tree produced by clipsparser#defglobal.
    def exitDefglobal(self, ctx: clipsparser.DefglobalContext):
        pass

    # Enter a parse tree produced by clipsparser#global_assignment.
    def enterGlobal_assignment(self, ctx: clipsparser.Global_assignmentContext):
        pass

    # Exit a parse tree produced by clipsparser#global_assignment.
    def exitGlobal_assignment(self, ctx: clipsparser.Global_assignmentContext):
        pass

    # Enter a parse tree produced by clipsparser#defrule.
    def enterDefrule(self, ctx: clipsparser.DefruleContext):
        pass

    # Exit a parse tree produced by clipsparser#defrule.
    def exitDefrule(self, ctx: clipsparser.DefruleContext):
        pass

    # Enter a parse tree produced by clipsparser#rule_name.
    def enterRule_name(self, ctx: clipsparser.Rule_nameContext):
        pass

    # Exit a parse tree produced by clipsparser#rule_name.
    def exitRule_name(self, ctx: clipsparser.Rule_nameContext):
        pass

    # Enter a parse tree produced by clipsparser#declaration.
    def enterDeclaration(self, ctx: clipsparser.DeclarationContext):
        pass

    # Exit a parse tree produced by clipsparser#declaration.
    def exitDeclaration(self, ctx: clipsparser.DeclarationContext):
        pass

    # Enter a parse tree produced by clipsparser#rule_property.
    def enterRule_property(self, ctx: clipsparser.Rule_propertyContext):
        pass

    # Exit a parse tree produced by clipsparser#rule_property.
    def exitRule_property(self, ctx: clipsparser.Rule_propertyContext):
        pass

    # Enter a parse tree produced by clipsparser#conditional_element.
    def enterConditional_element(self, ctx: clipsparser.Conditional_elementContext):
        pass

    # Exit a parse tree produced by clipsparser#conditional_element.
    def exitConditional_element(self, ctx: clipsparser.Conditional_elementContext):
        pass

    # Enter a parse tree produced by clipsparser#pattern_ce.
    def enterPattern_ce(self, ctx: clipsparser.Pattern_ceContext):
        pass

    # Exit a parse tree produced by clipsparser#pattern_ce.
    def exitPattern_ce(self, ctx: clipsparser.Pattern_ceContext):
        pass

    # Enter a parse tree produced by clipsparser#assigned_ce.
    def enterAssigned_ce(self, ctx: clipsparser.Assigned_ceContext):
        pass

    # Exit a parse tree produced by clipsparser#assigned_ce.
    def exitAssigned_ce(self, ctx: clipsparser.Assigned_ceContext):
        pass

    # Enter a parse tree produced by clipsparser#not_ce.
    def enterNot_ce(self, ctx: clipsparser.Not_ceContext):
        pass

    # Exit a parse tree produced by clipsparser#not_ce.
    def exitNot_ce(self, ctx: clipsparser.Not_ceContext):
        pass

    # Enter a parse tree produced by clipsparser#and_ce.
    def enterAnd_ce(self, ctx: clipsparser.And_ceContext):
        pass

    # Exit a parse tree produced by clipsparser#and_ce.
    def exitAnd_ce(self, ctx: clipsparser.And_ceContext):
        pass

    # Enter a parse tree produced by clipsparser#or_ce.
    def enterOr_ce(self, ctx: clipsparser.Or_ceContext):
        pass

    # Exit a parse tree produced by clipsparser#or_ce.
    def exitOr_ce(self, ctx: clipsparser.Or_ceContext):
        pass

    # Enter a parse tree produced by clipsparser#logical_ce.
    def enterLogical_ce(self, ctx: clipsparser.Logical_ceContext):
        pass

    # Exit a parse tree produced by clipsparser#logical_ce.
    def exitLogical_ce(self, ctx: clipsparser.Logical_ceContext):
        pass

    # Enter a parse tree produced by clipsparser#test_ce.
    def enterTest_ce(self, ctx: clipsparser.Test_ceContext):
        pass

    # Exit a parse tree produced by clipsparser#test_ce.
    def exitTest_ce(self, ctx: clipsparser.Test_ceContext):
        pass

    # Enter a parse tree produced by clipsparser#exists_ce.
    def enterExists_ce(self, ctx: clipsparser.Exists_ceContext):
        pass

    # Exit a parse tree produced by clipsparser#exists_ce.
    def exitExists_ce(self, ctx: clipsparser.Exists_ceContext):
        pass

    # Enter a parse tree produced by clipsparser#forall_ce.
    def enterForall_ce(self, ctx: clipsparser.Forall_ceContext):
        pass

    # Exit a parse tree produced by clipsparser#forall_ce.
    def exitForall_ce(self, ctx: clipsparser.Forall_ceContext):
        pass

    # Enter a parse tree produced by clipsparser#ordered_pattern.
    def enterOrdered_pattern(self, ctx: clipsparser.Ordered_patternContext):
        pass

    # Exit a parse tree produced by clipsparser#ordered_pattern.
    def exitOrdered_pattern(self, ctx: clipsparser.Ordered_patternContext):
        pass

    # Enter a parse tree produced by clipsparser#constaint.
    def enterConstaint(self, ctx: clipsparser.ConstaintContext):
        pass

    # Exit a parse tree produced by clipsparser#constaint.
    def exitConstaint(self, ctx: clipsparser.ConstaintContext):
        pass

    # Enter a parse tree produced by clipsparser#connected_constraint.
    def enterConnected_constraint(self, ctx: clipsparser.Connected_constraintContext):
        pass

    # Exit a parse tree produced by clipsparser#connected_constraint.
    def exitConnected_constraint(self, ctx: clipsparser.Connected_constraintContext):
        pass

    # Enter a parse tree produced by clipsparser#single_constraint.
    def enterSingle_constraint(self, ctx: clipsparser.Single_constraintContext):
        pass

    # Exit a parse tree produced by clipsparser#single_constraint.
    def exitSingle_constraint(self, ctx: clipsparser.Single_constraintContext):
        pass

    # Enter a parse tree produced by clipsparser#term.
    def enterTerm(self, ctx: clipsparser.TermContext):
        pass

    # Exit a parse tree produced by clipsparser#term.
    def exitTerm(self, ctx: clipsparser.TermContext):
        pass

    # Enter a parse tree produced by clipsparser#single_field_lhs.
    def enterSingle_field_lhs(self, ctx: clipsparser.Single_field_lhsContext):
        pass

    # Exit a parse tree produced by clipsparser#single_field_lhs.
    def exitSingle_field_lhs(self, ctx: clipsparser.Single_field_lhsContext):
        pass

    # Enter a parse tree produced by clipsparser#multi_field_lhs.
    def enterMulti_field_lhs(self, ctx: clipsparser.Multi_field_lhsContext):
        pass

    # Exit a parse tree produced by clipsparser#multi_field_lhs.
    def exitMulti_field_lhs(self, ctx: clipsparser.Multi_field_lhsContext):
        pass

    # Enter a parse tree produced by clipsparser#lhs_slot.
    def enterLhs_slot(self, ctx: clipsparser.Lhs_slotContext):
        pass

    # Exit a parse tree produced by clipsparser#lhs_slot.
    def exitLhs_slot(self, ctx: clipsparser.Lhs_slotContext):
        pass

    # Enter a parse tree produced by clipsparser#template_pattern.
    def enterTemplate_pattern(self, ctx: clipsparser.Template_patternContext):
        pass

    # Exit a parse tree produced by clipsparser#template_pattern.
    def exitTemplate_pattern(self, ctx: clipsparser.Template_patternContext):
        pass

    # Enter a parse tree produced by clipsparser#attribute_constraint.
    def enterAttribute_constraint(self, ctx: clipsparser.Attribute_constraintContext):
        pass

    # Exit a parse tree produced by clipsparser#attribute_constraint.
    def exitAttribute_constraint(self, ctx: clipsparser.Attribute_constraintContext):
        pass

    # Enter a parse tree produced by clipsparser#object_pattern.
    def enterObject_pattern(self, ctx: clipsparser.Object_patternContext):
        pass

    # Exit a parse tree produced by clipsparser#object_pattern.
    def exitObject_pattern(self, ctx: clipsparser.Object_patternContext):
        pass

    # Enter a parse tree produced by clipsparser#defmodule.
    def enterDefmodule(self, ctx: clipsparser.DefmoduleContext):
        pass

    # Exit a parse tree produced by clipsparser#defmodule.
    def exitDefmodule(self, ctx: clipsparser.DefmoduleContext):
        pass

    # Enter a parse tree produced by clipsparser#port_spec.
    def enterPort_spec(self, ctx: clipsparser.Port_specContext):
        pass

    # Exit a parse tree produced by clipsparser#port_spec.
    def exitPort_spec(self, ctx: clipsparser.Port_specContext):
        pass

    # Enter a parse tree produced by clipsparser#port_item.
    def enterPort_item(self, ctx: clipsparser.Port_itemContext):
        pass

    # Exit a parse tree produced by clipsparser#port_item.
    def exitPort_item(self, ctx: clipsparser.Port_itemContext):
        pass

    # Enter a parse tree produced by clipsparser#port_construct.
    def enterPort_construct(self, ctx: clipsparser.Port_constructContext):
        pass

    # Exit a parse tree produced by clipsparser#port_construct.
    def exitPort_construct(self, ctx: clipsparser.Port_constructContext):
        pass

    # Enter a parse tree produced by clipsparser#deffunction.
    def enterDeffunction(self, ctx: clipsparser.DeffunctionContext):
        pass

    # Exit a parse tree produced by clipsparser#deffunction.
    def exitDeffunction(self, ctx: clipsparser.DeffunctionContext):
        pass

    # Enter a parse tree produced by clipsparser#parameter.
    def enterParameter(self, ctx: clipsparser.ParameterContext):
        pass

    # Exit a parse tree produced by clipsparser#parameter.
    def exitParameter(self, ctx: clipsparser.ParameterContext):
        pass

    # Enter a parse tree produced by clipsparser#regular_para.
    def enterRegular_para(self, ctx: clipsparser.Regular_paraContext):
        pass

    # Exit a parse tree produced by clipsparser#regular_para.
    def exitRegular_para(self, ctx: clipsparser.Regular_paraContext):
        pass

    # Enter a parse tree produced by clipsparser#wildcard_para.
    def enterWildcard_para(self, ctx: clipsparser.Wildcard_paraContext):
        pass

    # Exit a parse tree produced by clipsparser#wildcard_para.
    def exitWildcard_para(self, ctx: clipsparser.Wildcard_paraContext):
        pass

    # Enter a parse tree produced by clipsparser#defclass.
    def enterDefclass(self, ctx: clipsparser.DefclassContext):
        pass

    # Exit a parse tree produced by clipsparser#defclass.
    def exitDefclass(self, ctx: clipsparser.DefclassContext):
        pass

    # Enter a parse tree produced by clipsparser#role.
    def enterRole(self, ctx: clipsparser.RoleContext):
        pass

    # Exit a parse tree produced by clipsparser#role.
    def exitRole(self, ctx: clipsparser.RoleContext):
        pass

    # Enter a parse tree produced by clipsparser#pattern_match_role.
    def enterPattern_match_role(self, ctx: clipsparser.Pattern_match_roleContext):
        pass

    # Exit a parse tree produced by clipsparser#pattern_match_role.
    def exitPattern_match_role(self, ctx: clipsparser.Pattern_match_roleContext):
        pass

    # Enter a parse tree produced by clipsparser#slot.
    def enterSlot(self, ctx: clipsparser.SlotContext):
        pass

    # Exit a parse tree produced by clipsparser#slot.
    def exitSlot(self, ctx: clipsparser.SlotContext):
        pass

    # Enter a parse tree produced by clipsparser#facet.
    def enterFacet(self, ctx: clipsparser.FacetContext):
        pass

    # Exit a parse tree produced by clipsparser#facet.
    def exitFacet(self, ctx: clipsparser.FacetContext):
        pass

    # Enter a parse tree produced by clipsparser#default_facet.
    def enterDefault_facet(self, ctx: clipsparser.Default_facetContext):
        pass

    # Exit a parse tree produced by clipsparser#default_facet.
    def exitDefault_facet(self, ctx: clipsparser.Default_facetContext):
        pass

    # Enter a parse tree produced by clipsparser#storage_facet.
    def enterStorage_facet(self, ctx: clipsparser.Storage_facetContext):
        pass

    # Exit a parse tree produced by clipsparser#storage_facet.
    def exitStorage_facet(self, ctx: clipsparser.Storage_facetContext):
        pass

    # Enter a parse tree produced by clipsparser#access_facet.
    def enterAccess_facet(self, ctx: clipsparser.Access_facetContext):
        pass

    # Exit a parse tree produced by clipsparser#access_facet.
    def exitAccess_facet(self, ctx: clipsparser.Access_facetContext):
        pass

    # Enter a parse tree produced by clipsparser#propagation_facet.
    def enterPropagation_facet(self, ctx: clipsparser.Propagation_facetContext):
        pass

    # Exit a parse tree produced by clipsparser#propagation_facet.
    def exitPropagation_facet(self, ctx: clipsparser.Propagation_facetContext):
        pass

    # Enter a parse tree produced by clipsparser#source_facet.
    def enterSource_facet(self, ctx: clipsparser.Source_facetContext):
        pass

    # Exit a parse tree produced by clipsparser#source_facet.
    def exitSource_facet(self, ctx: clipsparser.Source_facetContext):
        pass

    # Enter a parse tree produced by clipsparser#pattern_match_facet.
    def enterPattern_match_facet(self, ctx: clipsparser.Pattern_match_facetContext):
        pass

    # Exit a parse tree produced by clipsparser#pattern_match_facet.
    def exitPattern_match_facet(self, ctx: clipsparser.Pattern_match_facetContext):
        pass

    # Enter a parse tree produced by clipsparser#visibility_facet.
    def enterVisibility_facet(self, ctx: clipsparser.Visibility_facetContext):
        pass

    # Exit a parse tree produced by clipsparser#visibility_facet.
    def exitVisibility_facet(self, ctx: clipsparser.Visibility_facetContext):
        pass

    # Enter a parse tree produced by clipsparser#create_accessor_facet.
    def enterCreate_accessor_facet(self, ctx: clipsparser.Create_accessor_facetContext):
        pass

    # Exit a parse tree produced by clipsparser#create_accessor_facet.
    def exitCreate_accessor_facet(self, ctx: clipsparser.Create_accessor_facetContext):
        pass

    # Enter a parse tree produced by clipsparser#override_message_facet.
    def enterOverride_message_facet(self, ctx: clipsparser.Override_message_facetContext):
        pass

    # Exit a parse tree produced by clipsparser#override_message_facet.
    def exitOverride_message_facet(self, ctx: clipsparser.Override_message_facetContext):
        pass

    # Enter a parse tree produced by clipsparser#handler_document.
    def enterHandler_document(self, ctx: clipsparser.Handler_documentContext):
        pass

    # Exit a parse tree produced by clipsparser#handler_document.
    def exitHandler_document(self, ctx: clipsparser.Handler_documentContext):
        pass

    # Enter a parse tree produced by clipsparser#handler_type.
    def enterHandler_type(self, ctx: clipsparser.Handler_typeContext):
        pass

    # Exit a parse tree produced by clipsparser#handler_type.
    def exitHandler_type(self, ctx: clipsparser.Handler_typeContext):
        pass

    # Enter a parse tree produced by clipsparser#defgeneric.
    def enterDefgeneric(self, ctx: clipsparser.DefgenericContext):
        pass

    # Exit a parse tree produced by clipsparser#defgeneric.
    def exitDefgeneric(self, ctx: clipsparser.DefgenericContext):
        pass

    # Enter a parse tree produced by clipsparser#definstances.
    def enterDefinstances(self, ctx: clipsparser.DefinstancesContext):
        pass

    # Exit a parse tree produced by clipsparser#definstances.
    def exitDefinstances(self, ctx: clipsparser.DefinstancesContext):
        pass

    # Enter a parse tree produced by clipsparser#instance_template.
    def enterInstance_template(self, ctx: clipsparser.Instance_templateContext):
        pass

    # Exit a parse tree produced by clipsparser#instance_template.
    def exitInstance_template(self, ctx: clipsparser.Instance_templateContext):
        pass

    # Enter a parse tree produced by clipsparser#instance_definition.
    def enterInstance_definition(self, ctx: clipsparser.Instance_definitionContext):
        pass

    # Exit a parse tree produced by clipsparser#instance_definition.
    def exitInstance_definition(self, ctx: clipsparser.Instance_definitionContext):
        pass

    # Enter a parse tree produced by clipsparser#slot_override.
    def enterSlot_override(self, ctx: clipsparser.Slot_overrideContext):
        pass

    # Exit a parse tree produced by clipsparser#slot_override.
    def exitSlot_override(self, ctx: clipsparser.Slot_overrideContext):
        pass

    # Enter a parse tree produced by clipsparser#instances.
    def enterInstances(self, ctx: clipsparser.InstancesContext):
        pass

    # Exit a parse tree produced by clipsparser#instances.
    def exitInstances(self, ctx: clipsparser.InstancesContext):
        pass

    # Enter a parse tree produced by clipsparser#any_instancep.
    def enterAny_instancep(self, ctx: clipsparser.Any_instancepContext):
        pass

    # Exit a parse tree produced by clipsparser#any_instancep.
    def exitAny_instancep(self, ctx: clipsparser.Any_instancepContext):
        pass

    # Enter a parse tree produced by clipsparser#find_instance.
    def enterFind_instance(self, ctx: clipsparser.Find_instanceContext):
        pass

    # Exit a parse tree produced by clipsparser#find_instance.
    def exitFind_instance(self, ctx: clipsparser.Find_instanceContext):
        pass

    # Enter a parse tree produced by clipsparser#do_for_instance.
    def enterDo_for_instance(self, ctx: clipsparser.Do_for_instanceContext):
        pass

    # Exit a parse tree produced by clipsparser#do_for_instance.
    def exitDo_for_instance(self, ctx: clipsparser.Do_for_instanceContext):
        pass

    # Enter a parse tree produced by clipsparser#query.
    def enterQuery(self, ctx: clipsparser.QueryContext):
        pass

    # Exit a parse tree produced by clipsparser#query.
    def exitQuery(self, ctx: clipsparser.QueryContext):
        pass

    # Enter a parse tree produced by clipsparser#instance_set_template.
    def enterInstance_set_template(self, ctx: clipsparser.Instance_set_templateContext):
        pass

    # Exit a parse tree produced by clipsparser#instance_set_template.
    def exitInstance_set_template(self, ctx: clipsparser.Instance_set_templateContext):
        pass

    # Enter a parse tree produced by clipsparser#instance_set_member_template.
    def enterInstance_set_member_template(self, ctx: clipsparser.Instance_set_member_templateContext):
        pass

    # Exit a parse tree produced by clipsparser#instance_set_member_template.
    def exitInstance_set_member_template(self, ctx: clipsparser.Instance_set_member_templateContext):
        pass

    # Enter a parse tree produced by clipsparser#make_instance.
    def enterMake_instance(self, ctx: clipsparser.Make_instanceContext):
        pass

    # Exit a parse tree produced by clipsparser#make_instance.
    def exitMake_instance(self, ctx: clipsparser.Make_instanceContext):
        pass

    # Enter a parse tree produced by clipsparser#integer_expression.
    def enterInteger_expression(self, ctx: clipsparser.Integer_expressionContext):
        pass

    # Exit a parse tree produced by clipsparser#integer_expression.
    def exitInteger_expression(self, ctx: clipsparser.Integer_expressionContext):
        pass

    # Enter a parse tree produced by clipsparser#float_expression.
    def enterFloat_expression(self, ctx: clipsparser.Float_expressionContext):
        pass

    # Exit a parse tree produced by clipsparser#float_expression.
    def exitFloat_expression(self, ctx: clipsparser.Float_expressionContext):
        pass

    # Enter a parse tree produced by clipsparser#symbol_expression.
    def enterSymbol_expression(self, ctx: clipsparser.Symbol_expressionContext):
        pass

    # Exit a parse tree produced by clipsparser#symbol_expression.
    def exitSymbol_expression(self, ctx: clipsparser.Symbol_expressionContext):
        pass

    # Enter a parse tree produced by clipsparser#string_expression.
    def enterString_expression(self, ctx: clipsparser.String_expressionContext):
        pass

    # Exit a parse tree produced by clipsparser#string_expression.
    def exitString_expression(self, ctx: clipsparser.String_expressionContext):
        pass

    # Enter a parse tree produced by clipsparser#instancename_expression.
    def enterInstancename_expression(self, ctx: clipsparser.Instancename_expressionContext):
        pass

    # Exit a parse tree produced by clipsparser#instancename_expression.
    def exitInstancename_expression(self, ctx: clipsparser.Instancename_expressionContext):
        pass

    # Enter a parse tree produced by clipsparser#constant_expression.
    def enterConstant_expression(self, ctx: clipsparser.Constant_expressionContext):
        pass

    # Exit a parse tree produced by clipsparser#constant_expression.
    def exitConstant_expression(self, ctx: clipsparser.Constant_expressionContext):
        pass

    # Enter a parse tree produced by clipsparser#boolen_symbol.
    def enterBoolen_symbol(self, ctx: clipsparser.Boolen_symbolContext):
        pass

    # Exit a parse tree produced by clipsparser#boolen_symbol.
    def exitBoolen_symbol(self, ctx: clipsparser.Boolen_symbolContext):
        pass
