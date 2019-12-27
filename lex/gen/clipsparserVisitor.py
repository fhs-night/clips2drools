# Generated from E:/pycharm/repository/lex\clipsparser.g4 by ANTLR 4.7.2
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .clipsparser import clipsparser
else:
    from clipsparser import clipsparser


# This class defines a complete generic visitor for a parse tree produced by clipsparser.

class clipsparserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by clipsparser#prog.
    def visitProg(self, ctx: clipsparser.ProgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#variable.
    def visitVariable(self, ctx: clipsparser.VariableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#Expression_constant.
    def visitExpression_constant(self, ctx: clipsparser.Expression_constantContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#Expression_variable.
    def visitExpression_variable(self, ctx: clipsparser.Expression_variableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#Expression_functioncall.
    def visitExpression_functioncall(self, ctx: clipsparser.Expression_functioncallContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#Expression_conditionalelement.
    def visitExpression_conditionalelement(self, ctx: clipsparser.Expression_conditionalelementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#Expression_mathname.
    def visitExpression_mathname(self, ctx: clipsparser.Expression_mathnameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#Expression_predicate_name.
    def visitExpression_predicate_name(self, ctx: clipsparser.Expression_predicate_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#Expression_COMMENT.
    def visitExpression_COMMENT(self, ctx: clipsparser.Expression_COMMENTContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#action.
    def visitAction(self, ctx: clipsparser.ActionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#construct.
    def visitConstruct(self, ctx: clipsparser.ConstructContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#numeric_expression.
    def visitNumeric_expression(self, ctx: clipsparser.Numeric_expressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#singlefield_expression.
    def visitSinglefield_expression(self, ctx: clipsparser.Singlefield_expressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#multifield_expression.
    def visitMultifield_expression(self, ctx: clipsparser.Multifield_expressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#test_expression.
    def visitTest_expression(self, ctx: clipsparser.Test_expressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#comparison_expression.
    def visitComparison_expression(self, ctx: clipsparser.Comparison_expressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#lexeme_expression.
    def visitLexeme_expression(self, ctx: clipsparser.Lexeme_expressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#predicate_name.
    def visitPredicate_name(self, ctx: clipsparser.Predicate_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#connected_name.
    def visitConnected_name(self, ctx: clipsparser.Connected_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#math_name.
    def visitMath_name(self, ctx: clipsparser.Math_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#function_name.
    def visitFunction_name(self, ctx: clipsparser.Function_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#function_call.
    def visitFunction_call(self, ctx: clipsparser.Function_callContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#tradition_function.
    def visitTradition_function(self, ctx: clipsparser.Tradition_functionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#math_function.
    def visitMath_function(self, ctx: clipsparser.Math_functionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#predicate_function.
    def visitPredicate_function(self, ctx: clipsparser.Predicate_functionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#connected_function.
    def visitConnected_function(self, ctx: clipsparser.Connected_functionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#procedural_function.
    def visitProcedural_function(self, ctx: clipsparser.Procedural_functionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#if_then_else.
    def visitIf_then_else(self, ctx: clipsparser.If_then_elseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#while_do.
    def visitWhile_do(self, ctx: clipsparser.While_doContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#switch_stmt.
    def visitSwitch_stmt(self, ctx: clipsparser.Switch_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#foreach.
    def visitForeach(self, ctx: clipsparser.ForeachContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#loop_for_count.
    def visitLoop_for_count(self, ctx: clipsparser.Loop_for_countContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#return_stmt.
    def visitReturn_stmt(self, ctx: clipsparser.Return_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#break_stmt.
    def visitBreak_stmt(self, ctx: clipsparser.Break_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#case_stmt.
    def visitCase_stmt(self, ctx: clipsparser.Case_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#default_stmt.
    def visitDefault_stmt(self, ctx: clipsparser.Default_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#range_spec.
    def visitRange_spec(self, ctx: clipsparser.Range_specContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#deffacts.
    def visitDeffacts(self, ctx: clipsparser.DeffactsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#ordered_rhs_pattern.
    def visitOrdered_rhs_pattern(self, ctx: clipsparser.Ordered_rhs_patternContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#template_rhs_pattern.
    def visitTemplate_rhs_pattern(self, ctx: clipsparser.Template_rhs_patternContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#rhs_slot.
    def visitRhs_slot(self, ctx: clipsparser.Rhs_slotContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#single_field_rhs_slot.
    def visitSingle_field_rhs_slot(self, ctx: clipsparser.Single_field_rhs_slotContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#multi_field_rhs_slot.
    def visitMulti_field_rhs_slot(self, ctx: clipsparser.Multi_field_rhs_slotContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#rhs_field.
    def visitRhs_field(self, ctx: clipsparser.Rhs_fieldContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#rhs_pattern.
    def visitRhs_pattern(self, ctx: clipsparser.Rhs_patternContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#deftemplate.
    def visitDeftemplate(self, ctx: clipsparser.DeftemplateContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#slot_definition.
    def visitSlot_definition(self, ctx: clipsparser.Slot_definitionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#single_slot.
    def visitSingle_slot(self, ctx: clipsparser.Single_slotContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#multi_slot.
    def visitMulti_slot(self, ctx: clipsparser.Multi_slotContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#template_attr.
    def visitTemplate_attr(self, ctx: clipsparser.Template_attrContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#default_attr.
    def visitDefault_attr(self, ctx: clipsparser.Default_attrContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#constaint_attr.
    def visitConstaint_attr(self, ctx: clipsparser.Constaint_attrContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#type_attr.
    def visitType_attr(self, ctx: clipsparser.Type_attrContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#allowed_attr.
    def visitAllowed_attr(self, ctx: clipsparser.Allowed_attrContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#range_attr.
    def visitRange_attr(self, ctx: clipsparser.Range_attrContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#cardinality_attr.
    def visitCardinality_attr(self, ctx: clipsparser.Cardinality_attrContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#allowed_type.
    def visitAllowed_type(self, ctx: clipsparser.Allowed_typeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#class_name.
    def visitClass_name(self, ctx: clipsparser.Class_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#range_specification.
    def visitRange_specification(self, ctx: clipsparser.Range_specificationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#cardinality_specification.
    def visitCardinality_specification(self, ctx: clipsparser.Cardinality_specificationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#defglobal.
    def visitDefglobal(self, ctx: clipsparser.DefglobalContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#global_assignment.
    def visitGlobal_assignment(self, ctx: clipsparser.Global_assignmentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#defrule.
    def visitDefrule(self, ctx: clipsparser.DefruleContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#rule_name.
    def visitRule_name(self, ctx: clipsparser.Rule_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#declaration.
    def visitDeclaration(self, ctx: clipsparser.DeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#rule_property.
    def visitRule_property(self, ctx: clipsparser.Rule_propertyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#conditional_element.
    def visitConditional_element(self, ctx: clipsparser.Conditional_elementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#pattern_ce.
    def visitPattern_ce(self, ctx: clipsparser.Pattern_ceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#assigned_ce.
    def visitAssigned_ce(self, ctx: clipsparser.Assigned_ceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#not_ce.
    def visitNot_ce(self, ctx: clipsparser.Not_ceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#and_ce.
    def visitAnd_ce(self, ctx: clipsparser.And_ceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#or_ce.
    def visitOr_ce(self, ctx: clipsparser.Or_ceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#logical_ce.
    def visitLogical_ce(self, ctx: clipsparser.Logical_ceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#test_ce.
    def visitTest_ce(self, ctx: clipsparser.Test_ceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#exists_ce.
    def visitExists_ce(self, ctx: clipsparser.Exists_ceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#forall_ce.
    def visitForall_ce(self, ctx: clipsparser.Forall_ceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#ordered_pattern.
    def visitOrdered_pattern(self, ctx: clipsparser.Ordered_patternContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#constaint.
    def visitConstaint(self, ctx: clipsparser.ConstaintContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#connected_constraint.
    def visitConnected_constraint(self, ctx: clipsparser.Connected_constraintContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#single_constraint.
    def visitSingle_constraint(self, ctx: clipsparser.Single_constraintContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#term.
    def visitTerm(self, ctx: clipsparser.TermContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#single_field_lhs.
    def visitSingle_field_lhs(self, ctx: clipsparser.Single_field_lhsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#multi_field_lhs.
    def visitMulti_field_lhs(self, ctx: clipsparser.Multi_field_lhsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#lhs_slot.
    def visitLhs_slot(self, ctx: clipsparser.Lhs_slotContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#template_pattern.
    def visitTemplate_pattern(self, ctx: clipsparser.Template_patternContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#attribute_constraint.
    def visitAttribute_constraint(self, ctx: clipsparser.Attribute_constraintContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#object_pattern.
    def visitObject_pattern(self, ctx: clipsparser.Object_patternContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#defmodule.
    def visitDefmodule(self, ctx: clipsparser.DefmoduleContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#port_spec.
    def visitPort_spec(self, ctx: clipsparser.Port_specContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#port_item.
    def visitPort_item(self, ctx: clipsparser.Port_itemContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#port_construct.
    def visitPort_construct(self, ctx: clipsparser.Port_constructContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#deffunction.
    def visitDeffunction(self, ctx: clipsparser.DeffunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#parameter.
    def visitParameter(self, ctx: clipsparser.ParameterContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#regular_para.
    def visitRegular_para(self, ctx: clipsparser.Regular_paraContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#wildcard_para.
    def visitWildcard_para(self, ctx: clipsparser.Wildcard_paraContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#defclass.
    def visitDefclass(self, ctx: clipsparser.DefclassContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#role.
    def visitRole(self, ctx: clipsparser.RoleContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#pattern_match_role.
    def visitPattern_match_role(self, ctx: clipsparser.Pattern_match_roleContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#slot.
    def visitSlot(self, ctx: clipsparser.SlotContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#facet.
    def visitFacet(self, ctx: clipsparser.FacetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#default_facet.
    def visitDefault_facet(self, ctx: clipsparser.Default_facetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#storage_facet.
    def visitStorage_facet(self, ctx: clipsparser.Storage_facetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#access_facet.
    def visitAccess_facet(self, ctx: clipsparser.Access_facetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#propagation_facet.
    def visitPropagation_facet(self, ctx: clipsparser.Propagation_facetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#source_facet.
    def visitSource_facet(self, ctx: clipsparser.Source_facetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#pattern_match_facet.
    def visitPattern_match_facet(self, ctx: clipsparser.Pattern_match_facetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#visibility_facet.
    def visitVisibility_facet(self, ctx: clipsparser.Visibility_facetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#create_accessor_facet.
    def visitCreate_accessor_facet(self, ctx: clipsparser.Create_accessor_facetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#override_message_facet.
    def visitOverride_message_facet(self, ctx: clipsparser.Override_message_facetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#handler_document.
    def visitHandler_document(self, ctx: clipsparser.Handler_documentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#handler_type.
    def visitHandler_type(self, ctx: clipsparser.Handler_typeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#defgeneric.
    def visitDefgeneric(self, ctx: clipsparser.DefgenericContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#definstances.
    def visitDefinstances(self, ctx: clipsparser.DefinstancesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#instance_template.
    def visitInstance_template(self, ctx: clipsparser.Instance_templateContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#instance_definition.
    def visitInstance_definition(self, ctx: clipsparser.Instance_definitionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#slot_override.
    def visitSlot_override(self, ctx: clipsparser.Slot_overrideContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#instances.
    def visitInstances(self, ctx: clipsparser.InstancesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#any_instancep.
    def visitAny_instancep(self, ctx: clipsparser.Any_instancepContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#find_instance.
    def visitFind_instance(self, ctx: clipsparser.Find_instanceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#do_for_instance.
    def visitDo_for_instance(self, ctx: clipsparser.Do_for_instanceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#query.
    def visitQuery(self, ctx: clipsparser.QueryContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#instance_set_template.
    def visitInstance_set_template(self, ctx: clipsparser.Instance_set_templateContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#instance_set_member_template.
    def visitInstance_set_member_template(self, ctx: clipsparser.Instance_set_member_templateContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#make_instance.
    def visitMake_instance(self, ctx: clipsparser.Make_instanceContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#integer_expression.
    def visitInteger_expression(self, ctx: clipsparser.Integer_expressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#float_expression.
    def visitFloat_expression(self, ctx: clipsparser.Float_expressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#symbol_expression.
    def visitSymbol_expression(self, ctx: clipsparser.Symbol_expressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#string_expression.
    def visitString_expression(self, ctx: clipsparser.String_expressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#instancename_expression.
    def visitInstancename_expression(self, ctx: clipsparser.Instancename_expressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#constant_expression.
    def visitConstant_expression(self, ctx: clipsparser.Constant_expressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by clipsparser#boolen_symbol.
    def visitBoolen_symbol(self, ctx: clipsparser.Boolen_symbolContext):
        return self.visitChildren(ctx)


del clipsparser
