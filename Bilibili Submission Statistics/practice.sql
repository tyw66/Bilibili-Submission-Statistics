--ϵͳ�Դ��洢����
sp_databases
GO

sp_tables
GO

--�ҵ�һ���洢����,����ͳ�Ʋ���������
ALTER PROCEDURE ClassStatistics
	@NUMBER INT --�������,����OUTPUT
AS
BEGIN
	--����ע�������
	SELECT TOP (@NUMBER)  Big as '����' ,COUNT(av)as 'Ͷ����' ,SUM(PlayAmount) as '������' 
	FROM PlayList GROUP BY Big ORDER BY SUM(PlayAmount) DESC
END
GO

EXEC ClassStatistics 11

--SQL�����ϰ
SELECT * FROM PlayList

SELECT TOP 100 * FROM PlayList WHERE Big='����' ORDER BY PlayAmount DESC 

ALTER VIEW SANGUO AS(
	--������ͼ
	SELECT * FROM PlayList WHERE Title LIKE '%�����%'
	union
	SELECT * FROM PlayList WHERE Title LIKE '%˾��ܲ%'
	union
	SELECT * FROM PlayList WHERE Title LIKE '%��˾ͽ%'
	union
	SELECT * FROM PlayList WHERE Title LIKE '%����%'
)

--��ʼ����ı�־
BEGIN TRANSACTION  
	DELETE FROM PlayList WHERE AV='18898'
	DELETE FROM PlayList WHERE AV='18902'
--commitֻ������BEGIN TRANSACTION��,ֻ����䶼����ȷִ�к��commit���������������Զ�������	
COMMIT 

rollback