-- 코드를 입력하세요
SELECT count(*) from USER_INFO
WHERE year(JOINED) = '2021' and
AGE <= 29 and AGE >= 20;