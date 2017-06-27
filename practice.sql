--系统自带存储过程
sp_databases
GO

sp_tables
GO

--我的一个存储过程,分类统计播放量数据
ALTER PROCEDURE ClassStatistics
	@NUMBER INT --输入参数,不加OUTPUT
AS
BEGIN
	--变量注意加括号
	SELECT TOP (@NUMBER)  Big as '类型' ,COUNT(av)as '投稿数' ,SUM(PlayAmount) as '播放量' 
	FROM PlayList GROUP BY Big ORDER BY SUM(PlayAmount) DESC
END
GO

EXEC ClassStatistics 11

--SQL语句练习
SELECT * FROM PlayList

SELECT TOP 100 * FROM PlayList WHERE Big='鬼畜' ORDER BY PlayAmount DESC 

ALTER VIEW SANGUO AS(
	--建立视图
	SELECT * FROM PlayList WHERE Title LIKE '%诸葛亮%'
	union
	SELECT * FROM PlayList WHERE Title LIKE '%司马懿%'
	union
	SELECT * FROM PlayList WHERE Title LIKE '%王司徒%'
	union
	SELECT * FROM PlayList WHERE Title LIKE '%三国%'
)

--开始事务的标志
BEGIN TRANSACTION  
	DELETE FROM PlayList WHERE AV='18898'
	DELETE FROM PlayList WHERE AV='18902'
--commit只能用在BEGIN TRANSACTION后,只有语句都被正确执行后才commit，否则所做的事自动撤销。	
COMMIT 

rollback