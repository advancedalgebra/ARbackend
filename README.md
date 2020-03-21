## 基本情况

- 数据库：mysql
- 端口：120.79.19.172:3306
- 若不特别说明属性均为String类型、长度为40且非空，自增属性类型为Integer
- 暂时不使用外键约束
- 测试暂时以手动的方式进行

## Schema

### Building

- 属性：building_id、latitude、longitude、range（公差）、name、description
- latitude、longitude和range为float类型
- building_id为主键且自增
- description长度为400

### User

- 属性：username、password、token
- token长度为1000
- password长度为400
- username为主键

### event

- 属性：event_id、building_id、user_id、title、content、time
- event_id为主键且自增
- content长度为400

## 用户相关操作

headers统一都有

```json
{
  "content-type": "application/json"
}
```

### Register

1. url：/ar/api/auth/register  POST

2. Request（body）

   ```json
   {
     	"username": String,
     	"password": String,
   	“password_again”: String,
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
     	"username": String,
     	"oldPassword": String,
   	“newPassword”: String,
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
     	"username": String,
     	"password": String,
   }
   ```

3. Response（body）

   ```json
   {
     	"message": "ok",
       "token"：生成的token
   }
   ```

4. 检查错误：密码错误，用户名不存在

### Logout

1. url：/ar/api/auth/logout  POST

2. Request（headers）

   ```json
   {
     	"content-type": "application/json"
       "token": 自己的token
   }
   ```

3. Request（body）

   ```json
   {
     	"username": String,
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
     	"username": String,
     	"password": String,
   }
   ```

3. Response（body）

   ```json
   {
     	"message": "ok",
   }
   ```

4. 检查错误：密码错误，用户名不存在