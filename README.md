## 基本情况

- 数据库：mysql

- 端口：120.79.19.172:3306
- baseUrl：/ar/api
- 若不特别说明属性均为String类型、长度为40，自增属性类型为Integer
- 为方便测试，不使用外键约束

## Schema

### Building

- 属性：building_id、latitude、longitude、range（公差）、name、description
- latitude、longitude和range为float类型
- building_id为主键且自增
- description长度为400

### User

- 属性：user_id、username、password、token
- token长度为1000
- user_id为主键且自增

### event

- 属性：event_id、building_id、user_id、title、content、time
- event_id为主键且自增
- content长度为400

### 识别建筑

#### URL

GET /building/where?latitude=latitude&longitude=longitude&range=range

#### 说明

此接口用来通过用户位置判断要识别的建筑，返回建筑ID。若不能准确判断是哪个建筑，返回一个列表，按可信度排序

#### Request

##### Header:

```json
{
  "content-type": "application/json"
}
```

#### Response

##### Body:

```json
{
    [
    	"building_id": 0,
    	"name": 0,
    	"description": "",
    ]

}
```

##### 属性说明：

暂无

### 获取建筑信息

#### URL

GET /building/content?building_id=building_id

#### 说明

此接口通过建筑id获取建筑的信息，与上一接口是否合并成一个接口自行决定并修改此文件

#### Request

##### Header:

```json
{
  "content-type": "application/json"
}
```

#### Response

##### Body:

```json
{
    "building_id": 0,
    "name": 0,
    "description": "",
}
```

##### 属性说明：

暂无

## 用户相关操作

### Login

1. url：POST /auth/login

#### Request
##### header
```json
{
  "content-type": "application/json"
}
```
#### body
```json
{
  "username": "xxx",
  "password": "xxx"
}
```
### Response
#### body
```json
{
  "message": "xxx",
  "token": ""
}
```
### Register

#### url

POST /auth/register

#### Request
##### header
```json
{
  "content-type": "application/json"
}
```
##### body
```json
{
  "username": "xxx",
  "password": "xxx",
  "student_id": "xxx"
}
```
#### Response
##### body
```json
{
  "message": "xxx",
}
```

## Test