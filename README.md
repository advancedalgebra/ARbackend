## 基本情况

- 数据库：mysql

- 端口：120.79.19.172:3306

- 若不特别说明属性均为String类型、长度为40且非空，自增属性类型为Integer

- headers统一都有

  ```json
  {
    "content-type": "application/json"
  }
  ```

- 暂时不使用外键约束

- 测试暂时以手动的方式进行

## Schema

### Building

- 属性：building_id、latitude_upper 、longitude_upper、latitude_lower、longitude_lower、name、description
- latitude_upper 、longitude_upper、latitude_lower、longitude_lower为float类型，指示建筑范围
- building_id为主键且自增
- description长度为1000

### User

- 属性：username、password、token
- token长度为1000
- password长度为400
- username为主键

### event

- 属性：event_id、building_id、username、title、content、time
- event_id为主键且自增
- building_id为Integer类型
- content长度为400

## 用户相关操作

### Register

1. url：/ar/api/auth/register  POST

2. Request（body）

   ```json
   {
     "username": "string",
     "password": "string",
     "password_again": "string",
   }
   ```

3. Response（body）

   ```json
   {
     "message": "ok",
   }
   ```

4. 检查错误：用户名重复、密码不一致

### Change Password

1. url：/ar/api/auth/password  POST

2. Request（body）

   ```json
   {
     "username": "string",
     "oldPassword": "string",
     "newPassword": "string",
   }
   ```

3. Response（body）

   ```json
   {
     "message": "ok",
   }
   ```

4. 检查错误：旧密码错误，用户名不存在

### Login

1. url：/ar/api/auth/login  POST

2. Request（body）

   ```json
   {
     "username": "string",
     "password": "string",
   }
   ```

3. Response（body）

   ```json
   {
     "message": "ok",
     "token": "生成的token"
   }
   ```

4. 检查错误：密码错误，用户名不存在

### Logout

1. url：/ar/api/auth/logout  POST

2. Request（headers）

   ```json
   {
     "content-type": "application/json",
     "token": "自己的token"
   }
   ```

3. Request（body）

   ```json
   {
     "username": "string",
   }
   ```

4. Response（body）

   ```json
   {
     "message": "ok",
   }
   ```

4. 检查错误：用户名错误、token错误、重复登出

### Unregister

1. url：/ar/api/auth/unregister  POST

2. Request（body）

   ```json
   {
     "username": "string",
     "password": "string",
   }
   ```

3. Response（body）

   ```json
   {
     "message": "ok",
   }
   ```

4. 检查错误：密码错误，用户名不存在

## 建筑相关操作

### 识别建筑

1. url：/ar/api/location/building_id  POST

2. Request（body）

   ```json
   {
     "latitude": "float",
     "latitude": "float",
   }
   ```

3. Response（body）

   ```json
   {
     "message": "list",
   }
   ```

   返回一个元素为字典的列表，列表中包含所有可能的建筑，每一个字典包含建筑的id和名字

4. 检查错误：建筑不存在

### 获取建筑信息

1. url：/ar/api/location/building_detail  POST

2. Request（body）

   ```json
   {
     "building_id": "Integer",
   }
   ```

3. Response（body）

   ```json
   {
     "message": "建筑的描述",
   }
   ```

4. 检查错误：建筑不存在

### 针对上两个的token版

1. url：/ar/api/location/building_detail_token  POST        url：/ar/api/location/building_id_token  POST
2. Request（headers）加上token，Request（body）加上username其余不变
3. 检查错误：建筑不存在、用户名错误、token错误