Table Account
------------------
name String
username String (可使用工号登录)（主键）
password String(AES256)
phone String(AES256)（可使用手机号码登录）（唯一索引）
email String(AES256)（可使用电子邮箱登录）（唯一索引）
group String
sex String
arch_group String
ctime DateTime
utime DateTime
is_delete Boolean

Table Group
------------------
name String（主键）
ctime DateTime
usage String
utime DateTime
is_delete Boolean

Table Machine
------------------
id UUID String (主键)
type String
machine-group String
res-pool String
safe-group
ctime DateTime
utime DateTime
status String
is_delete Boolean

Table MachineGroup
------------------
name String（主键）
level String
parent-group Stirng
ctime DateTime
utime DateTime
biz-needs String
is_delete Boolean

Table SafeGroup 
------------------
name String （主键）
ports List
ctime DateTime
utime DateTime
biz-needs String
is_delete Boolean

Table ResPool
------------------
name String（主键）
memory Integer
proccessor Integer
storage Float
network Float
ctime DateTime
utime DateTime
biz-needs String
is_delete Boolean

Table Config
-----------------
name String （主键）
type String
address String
ctime DateTime
utime DateTime
biz-needs String

Table Audit
-----------------
level String
uid UUID String
result String
ctime DateTime
utime DateTime
event String

Table Task
-----------------
id UUID String （主键）
repo String
branch String
tag String
target_machine List
target_group List
target_directory String
post-sync-script String
webhook-url String
webhook-sign String
logs String
ctime DateTime
utime DateTime
is_delete Boolea
status String
timeout DateTime (当timeout == null 表示没有超时限制)
retry Integer (默认3次)

Table TaskDetail
-----------------
task_id UUID String
machine_id UUID String
status String
ctime DateTime
utime DateTime