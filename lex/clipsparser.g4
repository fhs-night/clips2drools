parser grammar clipsparser;
//options{language = python ;tokenVocab = clipslexer; }
options{tokenVocab = clipslexer; }

//clips语法

//起始规则
prog : (expression | construct)*;
construct : defrule | deffacts | defglobal | deftemplate | deffunction | defmodule | defclass | defgeneric
          | definstances;
//表达式
expression : constant_expression     # Expression_constant
            | variable               # Expression_variable
            | function_call          # Expression_functioncall
            | conditional_element    # Expression_conditionalelement
            | math_name              # Expression_mathname
            | predicate_name        # Expression_predicate_name
            | COMMENT               #Expression_COMMENT
            ;
action : expression;
//变量类型
variable : Global_var | Single_field_var | Multi_field_var;
//中级表达式
numeric_expression : integer_expression | float_expression;
singlefield_expression :constant_expression
                        | function_name
                        | predicate_name | math_name | connected_name
                        ;//原始数据类型:INT FLOAT SYMBOL
                        //还有未定义instance_addressfact_addressexternal_address
multifield_expression : '(' singlefield_expression* ')';
test_expression : variable;
comparison_expression : Global_var
                      | constant_expression
                      | predicate_name
                      | math_name
                      | connected_name
                      ;
lexeme_expression : string_expression | symbol_expression;

predicate_name : EQ | NEQ | '=' | '<>' | '>' | '>=' | '<' |'<=';
connected_name : AND | OR | NOT;
math_name : '+' | '-' | '*' | '/' | Int_div | FLOAT | INTEGER | '**' | MOD;
function_name : symbol_expression;
function_call :tradition_function
              | procedural_function
              | instances
              | math_function
              | connected_function
              | predicate_function
              ;
tradition_function : '(' function_name expression* ')';
math_function : '(' math_name expression* ')';
predicate_function : '(' predicate_name expression* ')';
connected_function : '(' connected_name expression+ ')';
procedural_function : if_then_else | while_do | switch_stmt | foreach | loop_for_count | return_stmt | break_stmt;
//procedural function
if_then_else : '(' IF expression COMMENT* THEN action* (ELSE action*)? ')';
while_do : '(' WHILE expression DO? action* ')';
switch_stmt : '(' SWITCH test_expression case_stmt* default_stmt? ')';
foreach : '(' FOREACH variable multifield_expression expression* ')';
loop_for_count : '(' LOOPFORCOUNT range_spec DO? action* ')';
return_stmt : '(' RETURN expression? ')';
break_stmt : '(' BREAK ')';
case_stmt : '(' CASE comparison_expression THEN action* ')';
default_stmt : '(' DEFAULT action* ')';
range_spec : integer_expression
            | '(' variable integer_expression integer_expression ')'
            | '(' variable integer_expression ')'
            ;

//结构
//deffacts
deffacts : '(' DEFFACT symbol_expression string_expression? rhs_pattern* ')';
ordered_rhs_pattern : '(' symbol_expression rhs_field+ ')';
template_rhs_pattern : '(' symbol_expression rhs_slot ')';
rhs_slot : single_field_rhs_slot | multi_field_rhs_slot;
single_field_rhs_slot : '(' symbol_expression rhs_field ')';
multi_field_rhs_slot : '(' symbol_expression rhs_field* ')';
rhs_field : variable | constant_expression | function_call;
rhs_pattern : ordered_rhs_pattern | template_rhs_pattern;
//deftemplate
deftemplate : '(' DEFTEMPLATE symbol_expression string_expression? slot_definition* ')';
slot_definition : single_slot | multi_slot;
single_slot : '(' SLOT symbol_expression template_attr* ')';
multi_slot : '(' MULTISLOT symbol_expression template_attr* ')';
template_attr : default_attr | constaint_attr;
default_attr : '(' DEFAULT (DERIVE | NONE | expression*) ')'
                | '(' DEFAULTDYNAMIC expression* ')';
constaint_attr : type_attr | allowed_attr | range_attr | cardinality_attr;
type_attr : '(' TYPE (allowed_type+ | VARIABLE) ')';
allowed_attr : '(' ALLOWEDSYMBOLS (symbol_expression+ | VARIABLE) ')'
             | '(' ALLOWEDSTRINGS (string_expression+ | VARIABLE) ')'
             | '(' ALLOWEDLEXEMES (lexeme_expression+ | VARIABLE) ')'
             | '(' ALLOWEDINTEGERS (integer_expression+ | VARIABLE) ')'
             | '(' ALLOWEDFLOATS  (float_expression+ | VARIABLE) ')'
             | '(' ALLOWEDNUMBERS (numeric_expression+ | VARIABLE) ')'
             | '(' ALLOWEDINSTANCESNAMES (instancename_expression+ | VARIABLE) ')'
             | '(' ALLOWEDCLASSES ( class_name| VARIABLE) ')'
             | '(' ALLOWEDVALUES (constant_expression+ | VARIABLE) ')'
             ;
range_attr : '(' RANGE range_specification range_specification ')';
cardinality_attr : '(' CARDINALITY cardinality_specification cardinality_specification ')';
allowed_type : CAPSYMBOL | CAPSTRING | LEXEME | CAPINTEGER
                | CAPFLOAT | NUMBER
                | INSTANCENAME | INSTANCEADDRESS | CAPINSTANCE
                | EXTERNALADDRESS | FACTADDRESS
                ;
class_name : symbol_expression;
range_specification : numeric_expression | VARIABLE;
cardinality_specification : integer_expression | VARIABLE;
//defglobal
defglobal : '(' DEFGLOBAL symbol_expression? global_assignment* ')';
global_assignment : Global_var '=' expression;

//defrule结构体语法格式
defrule : '(' DEFRULE rule_name string_expression?
            declaration? conditional_element*
            '=>'
            action* ')'
            ;

rule_name : symbol_expression;
declaration : '(' DECLARE rule_property+ ')';
rule_property : '(' SALIENCE integer_expression ')'
                | '(' AUTOFOCUS boolen_symbol ')'
                ;

//conditional_element
conditional_element :pattern_ce
                    | assigned_ce
                    | not_ce | and_ce | or_ce
                    | logical_ce | test_ce
                    | exists_ce | forall_ce
                    ;
pattern_ce : ordered_pattern | template_pattern | object_pattern;
assigned_ce : Single_field_var '<-' pattern_ce;
not_ce : '(' NOT conditional_element ')';
and_ce :'(' AND conditional_element+ ')';
or_ce : '(' OR conditional_element+ ')';
logical_ce :'(' LOGICAL conditional_element+ ')';
test_ce : '(' TEST function_call ')';
exists_ce : '(' EXISTS conditional_element+ ')';
forall_ce : '(' FORALL conditional_element conditional_element+ ')';
ordered_pattern : '(' symbol_expression constaint* ')';
constaint : '?' | '$?' | connected_constraint;
connected_constraint : single_constraint
                     | single_constraint '&' connected_constraint
                     | single_constraint '|' connected_constraint
                     ;
single_constraint: term | '~'term;
term : constant_expression
        | Single_field_var
        | Multi_field_var
        | (':' function_call)
        | ('=' function_call)
        ;
single_field_lhs : '(' symbol_expression constaint ')';
multi_field_lhs : '(' symbol_expression constaint* ')';
lhs_slot : single_field_lhs | multi_field_lhs;
template_pattern : '(' symbol_expression lhs_slot* ')';
attribute_constraint : '(' ISA constaint ')'
                     //| '(' 'name' constaint ')'
                     | '(' symbol_expression constaint* ')'
                     ;
object_pattern : '(' OBJECT attribute_constraint* ')';


//defmodule
defmodule : '(' DEFMODULE symbol_expression string_expression?
                port_spec* ')'
          ;
port_spec : '(' EXPORT port_item ')'
          | '(' IMPORT symbol_expression port_item ')'
          ;
port_item : ALL
          | NONE
          | port_construct ALL
          | port_construct NONE
          | port_construct symbol_expression+
          ;
port_construct : DEFTEMPLATE | DEFCLASS | DEFGLOBAL | DEFFUNCTION | DEFGENERIC;

//deffunction结构体语法格式
deffunction : '(' DEFFUNCTION symbol_expression string_expression?
                    parameter
                    action* ')'
            ;

parameter : '(' regular_para* wildcard_para? ')';
regular_para : Single_field_var;
wildcard_para : Multi_field_var;
//defclass
defclass : '(' DEFCLASS symbol_expression string_expression?
                   '(' ISA symbol_expression+ ')'
                   role?
                   pattern_match_role?
                   slot*
                   handler_document* ')'
         ;
role : '(' ROLE (CONCRETE | ABSTRACT) ')';
pattern_match_role : '(' PATTERNMATCH (REACTIVE | NONREACTIVE) ')';
slot : '(' SLOT symbol_expression facet* ')'
     | '(' SINGLESLOT symbol_expression facet* ')'
     | '(' MULTISLOT symbol_expression facet* ')'
     ;
facet : default_facet  | constaint_attr
      | template_attr
      | storage_facet | access_facet | propagation_facet
      | source_facet | pattern_match_facet | visibility_facet
      | create_accessor_facet | override_message_facet
      ;
default_facet : '(' DEFAULT (DERIVE | NONE | expression*) ')'
              | '(' 'default-dynamic' expression* ')'
              ;

storage_facet : '(' 'storage' ('local' | 'shared') ')';
access_facet : '(' 'access' ('read-write' | 'read-only' | 'initialize-only') ')';
propagation_facet : '(' 'propagation' ('inherit' | 'no-inherit') ')';
source_facet : '(' 'source' ('exclusive' | 'composite') ')';
pattern_match_facet : '(' 'pattern-match' ('reactive' | 'non-reactive') ')';
visibility_facet : '(' 'visibility' ('private' | 'public') ')';
create_accessor_facet : '(' CREATEACCESSOR (NONE | READ | WRITE | READWRITE) ')';
override_message_facet : '(' 'override-message' ('?DEFAULT' | symbol_expression) ')';
handler_document : '(' 'message-handler' symbol_expression handler_type? ')';
handler_type : 'primary' | 'around' | 'before' | 'after';

//defgeneric
defgeneric : '(' DEFGENERIC symbol_expression string_expression? ')';

//definstance
definstances : '(' DEFINSTANCES symbol_expression ACTIVE? string_expression?
                 instance_template* ')';
instance_template : '(' instance_definition ')';
instance_definition : symbol_expression? OF class_name slot_override*;
slot_override : '(' symbol_expression expression* ')';
//instance函数
instances : any_instancep | find_instance | do_for_instance | make_instance;
any_instancep : '(' 'any-instancep' instance_set_template query ')';
find_instance : '(' ('find-instance' | 'find-all-instances')
                        instance_set_template query ')';
do_for_instance : '(' ('do-for-instance' | 'do-for-all-instances' | 'delayed-do-for-all-instances')
                        instance_set_template query action* ')';
query : expression | TRUE | FALSE;
instance_set_template : '(' instance_set_member_template+ ')';
instance_set_member_template : '(' Single_field_var class_name+ ')';
make_instance : '(' ('make-instance' | 'active-make-instance') instance_definition')';

//初级表达式
integer_expression : Int_number;
float_expression : Float_number;
symbol_expression : boolen_symbol | PRIMARY | ID ;
string_expression : STRING_literal;
instancename_expression : INSTANCE_name;
constant_expression : integer_expression | float_expression | symbol_expression
                    | string_expression  | instancename_expression;//常量
boolen_symbol : TRUE | FALSE | NULL;


//未定义
/*
external_address : ;//
fact_address : ;
instance_address :;
defmethod :
defmessage :;*/