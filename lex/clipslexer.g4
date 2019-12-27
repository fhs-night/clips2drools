lexer grammar clipslexer;
options{language = python ;}

//数据类型
FLOAT : 'float';
INTEGER : 'integer';
SYMBOL : 'symbol';
STRING : 'string';
ADDRESS : 'address';
INSTANCE : 'instance';
EXTERNAL : 'external';
FACT : 'fact';
CAPFLOAT : 'FLOAT';
CAPINTEGER : 'INTEGER';
CAPSYMBOL : 'SYMBOL';
CAPINSTANCE : 'INSTANCE';
CAPSTRING : 'STRING';
LEXEME : 'LEXEME';
NUMBER : 'NUMBER';
INSTANCENAME : 'INSTANCE-NAME';
INSTANCEADDRESS : 'INSTANCE-ADDRESS';
EXTERNALADDRESS : 'EXTERNAL-ADDRESS';
FACTADDRESS : 'FACT-ADDRESS';

//关键字
WHILE : 'while';
DO : 'do';
IF : 'if';
THEN : 'then';
ELSE : 'else';
RETURN : 'return';
SWITCH : 'switch';
FOREACH : 'foreach';
OR : 'or';
EQ : 'eq';
NEQ : 'neq';
AND : 'and';
TEST : 'test';
NOT : 'not';
MOD : 'mod';
DECLARE : 'declare';
LOGICAL : 'logical';
OBJECT : 'object';
EXISTS : 'exists';
FORALL : 'forall';
BREAK : 'break';
CASE : 'case';
DEFAULT : 'default';
CAPDEFAULT : '?DEFAULT';
LOOPFORCOUNT : 'loop-for-count';
TRUE : 'TRUE';
FALSE : 'FALSE';
NULL : 'NULL';
DEFFACT : 'deffacts';
DEFTEMPLATE : 'deftemplate';
DEFGLOBAL : 'defglobal';
DEFRULE : 'defrule';
DEFFUNCTION : 'deffunction';
DEFMODULE : 'defmodule';
DEFGENERIC : 'defgeneric';
DEFCLASS : 'defclass';
DEFINSTANCES : 'definstances';
SLOT : 'slot';
MULTISLOT : 'multislot';
ALLOWEDSYMBOLS : 'allowed-symbols';
ALLOWEDSTRINGS : 'allowed-strings';
ALLOWEDLEXEMES : 'allowed-lexemes';
ALLOWEDINTEGERS : 'allowed-integers';
ALLOWEDFLOATS : 'allowed-floats';
ALLOWEDNUMBERS : 'allowed-numbers';
ALLOWEDINSTANCESNAMES : 'allowed-instances-names';
ALLOWEDCLASSES : 'allowed-classes';
ALLOWEDVALUES : 'allowed-values';
VARIABLE : '?VARIABLE';
RANGE : 'range';
CARDINALITY : 'cardinality';
TYPE : 'type';
DERIVE : '?DERIVE';
NONE : '?NONE';
DEFAULTDYNAMIC : 'default-dynamic';
SALIENCE : 'salience';
AUTOFOCUS : 'auto-focus';
ISA : 'is-a';
ACTIVE :'active';
//NAME : 'name';
EXPORT : 'export';
IMPORT : 'import';
ALL : '?ALL';
ROLE : 'role';
CONCRETE : 'concrete';
ABSTRACT : 'abstract';
PATTERNMATCH : 'pattern-match';
REACTIVE : 'reactive';
NONREACTIVE : 'non-reactive';
SINGLESLOT : 'single-slot';
STORAGE : 'storage';
LOCAL : 'local';
SHARED : 'shared';
ACCESS : 'access';
READWRITE : 'read-write';
READONLY : 'read-only';
INITIALIZEONLY : 'initialize-only';
PROPAGATION : 'propagation';
INHERIT : 'inherit';
NOINHERIT : 'no-inherit';
SOURCE : 'source';
EXCLUSIVE : 'exclusive';
COMPOSITE : 'composite';
VISIBILITY : 'visibility';
PRIVATE : 'private';
PUBLIC : 'public';
CREATEACCESSOR : 'create-accessor';
READ :'read';
WRITE : 'write';
OVERRIDDEMESSAGE : 'override-message';
MESSAGEHANDLER : 'message-handler';
PRIMARY :'primary';
AROUND : 'around';
BEFORE :'before';
AFTER : 'after';
OF : 'of';
ANYINSTANCEP : 'any-instancep';
FINDINSTANCE : 'find-instance';
FINDALLINSTANCES : 'find-all-instances';
DOFORINSTANCE : 'do-for-instance';
DOFORALLINSTANCES : 'do-for-all-instances';
DELAYEDINSTANCES : 'delayed-do-for-all-instances';
MAKEINSTANCE : 'make-instance';
ACTIVEMAKEINSTANCE :'active-make-instance';
//符号
Ellipsis : '...';
LeftParen : '(';
RightParen : ')';
LeftBracket : '[';
RightBracket : ']';
Less : '<';
QUESTION: '?';
LessEqual : '<=';
Greater : '>';
GreaterEqual : '>=';
LessGreater : '<>';
Plus : '+';
Minus : '-';
Mul : '*';
Power : '**';
Connect_and : '&';
Connection : '$';
QUESCON : '$?';
Connect_or : '|';
Connect_not : '~';
Div : '/' ;//不取整
Int_div : 'div';//相除后取整
LessArrow : '<-';
Colon : ':';
Semi : ';';
Assign : '=';
RightAssign : '=>';

//基本数据类型格式
Int_number : [+-]? DIGIT+;  // 匹配整型数字
Float_number : [+-]? DIGIT+ ('.')? (DIGIT+)? Exponent?;  // 匹配浮点型数字
//所有可打印ASCII码,除'\t','<',';','&','(',')','|','~','"'
ID : ID_Start ID_Continue*;
STRING_literal:     '"' (ESC|.)*?  '"';
INSTANCE_name : '[' ID ']';
//数字
DIGIT : [0-9];
Exponent : [Ee] [+-]? DIGIT+;

//变量名
Variable_symbol : ([a-zA-Z] ID_Continue*);
Global_var : '?' '*' ID '*';
Single_field_var : '?' Variable_symbol;
Multi_field_var : '$' '?' Variable_symbol;
//空白 注释
WS:                 [ \t\r\n\u000C]+ -> channel(1);
COMMENT:            ';' .*? '\n';//  -> channel(2);

fragment ID_Continue : '\u0021' | [\u0023-\u0025] | '\u0027' | [\u002A-\u003A] | [\u003D-\u007B] | '\u007D';
fragment ID_Start : '\u0021' | '\u0023' | '\u0025' | '\u0027'
                  | [\u002A-\u003A]
                  | [\u003C-\u003E]
                  | [\u0040-\u007B]
                  | '\u007D'
                  ;//首字母不能有'$','?'
fragment ESC : '\\"';







