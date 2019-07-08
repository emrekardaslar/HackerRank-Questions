SELECT 
CASE 
WHEN A+B>C AND A+C>B AND B+C>A THEN 
    CASE 
    WHEN A=B AND B=C THEN 'Equilateral'
    WHEN A=B OR B=A OR C=A THEN 'Isosceles'
    WHEN A!=B OR B!=C OR C!=A THEN 'Scalene'
    END
    ELSE 'Not A Triangle'
END FROM TRIANGLES;
