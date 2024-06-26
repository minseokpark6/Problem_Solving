# [level 2] 자동차 종류 별 특정 옵션이 포함된 자동차 수 구하기 - 151137 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/151137) 

### 제출 일자

2024년 04월 17일 08:51:23

### 문제 설명

<p>다음은 어느 자동차 대여 회사에서 대여중인 자동차들의 정보를 담은 <code>CAR_RENTAL_COMPANY_CAR</code> 테이블입니다. <code>CAR_RENTAL_COMPANY_CAR</code> 테이블은 아래와 같은 구조로 되어있으며, <code>CAR_ID</code>, <code>CAR_TYPE</code>, <code>DAILY_FEE</code>, <code>OPTIONS</code> 는 각각 자동차 ID, 자동차 종류, 일일 대여 요금(원), 자동차 옵션 리스트를 나타냅니다.</p>
<table class="table">
        <thead><tr>
<th>Column name</th>
<th>Type</th>
<th>Nullable</th>
</tr>
</thead>
        <tbody><tr>
<td>CAR_ID</td>
<td>INTEGER</td>
<td>FALSE</td>
</tr>
<tr>
<td>CAR_TYPE</td>
<td>VARCHAR(255)</td>
<td>FALSE</td>
</tr>
<tr>
<td>DAILY_FEE</td>
<td>INTEGER</td>
<td>FALSE</td>
</tr>
<tr>
<td>OPTIONS</td>
<td>VARCHAR(255)</td>
<td>FALSE</td>
</tr>
</tbody>
      </table>
<p>자동차 종류는 '세단', 'SUV', '승합차', '트럭', '리무진' 이 있습니다. 자동차 옵션 리스트는 콤마(',')로 구분된 키워드 리스트(옵션 리스트 값 예시: '열선시트', '스마트키', '주차감지센서')로 되어있으며, 키워드 종류는 '주차감지센서', '스마트키', '네비게이션', '통풍시트', '열선시트', '후방카메라', '가죽시트' 가 있습니다.</p>

<hr>

<h5>문제</h5>

<p><code>CAR_RENTAL_COMPANY_CAR</code> 테이블에서 '통풍시트', '열선시트', '가죽시트' 중 하나 이상의 옵션이 포함된 자동차가 자동차 종류 별로 몇 대인지 출력하는 SQL문을 작성해주세요. 이때 자동차 수에 대한 컬럼명은 <code>CARS</code>로 지정하고, 결과는 자동차 종류를 기준으로 오름차순 정렬해주세요.</p>

<hr>

## 💡Solving
```sql
select CAR_TYPE, count(CAR_ID) as CARS
from CAR_RENTAL_COMPANY_CAR
where OPTIONS like "%통풍시트%" or OPTIONS like "%가죽시트%" or OPTIONS like "%열선시트%"
group by 1
order by 1;
```

<br />

## Solving_Wrong

```sql
select CAR_TYPE, count(CAR_ID) as CARS
from CAR_RENTAL_COMPANY_CAR
where OPTIONS in ("통풍시트", "가죽시트", "열선시트")
group by 1
order by 1;
```

<br />

## 💡Review
* Option 컬럼의 데이터를 보면 ',' Comma로 연결되어 있는 것이 개별적인 단어로 인식되는 것이 아니라 하나의 문자열로 인식됨.
  <br />
  ==> 그렇기 때문에 in 연산자를 사용하는 대신, 문자열에서 특정 문자 포함 여부를 찾는 like "%" 연산자를 사용하는 것이 맞음
