Simplified Modula2 Interpreter
============

A minimal form of Modula2, has only 1 data type and single letter identifiers.


Grammar
-------

Parser

    <program> → MODULE <id> ; BEGIN <statement_sequence> END <id> .
    <statement_sequence> → <statement> ; | <statement_sequence>  <statement> ;
    <statement> → <assignment_statement> | <print_statement> | <while_statement> | <if_statement> | <until_statement>
    <if_statement> → IF <boolean_expression> THEN <statement_sequence> ELSE <statement_sequence> END 
    <while_statement> → WHILE <boolean_expression> DO  <statement_sequence>  END 
    <assignment_statement> → <id> assignment_operator <expression>
    <print_statement> → WriteInt  ( <expression>  )
    <until_statement> → REPEAT <statement_sequence> UNTIL <boolean_expression>  
    <boolean_expression> → <relational_operator> <expression> <expression>
    <relational_operator> → le_operator | lt_operator | ge_operator | gt_operator | eq_operator | ne_operator
    <expression> → <arithmetic_operator> <expression> <expression> | <id> | literal_integer
    <arithmetic_operator> → add_operator | sub_operator | mul_operator | div_operator

Lexical Analyzer

    id → letter
    literal_integer → digit literal_integer | digit
    assignment_operator → :=
    le_operator → <=
    lt_operator → <
    ge_operator → >=
    gt_operator → >
    eq_operator → =
    ne_operator → #
    add_operator → +
    sub_operator → -
    mul_operator → *
    div_operator → /
