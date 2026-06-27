class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # 1. 빈도수 맵 생성
        m = {}
        for k in nums:
            m[k] = m.get(k, 0) + 1
            
        # 2. 숫자 '1'에 대한 예외 처리
        if 1 in m:
            ans = m[1] if m[1] % 2 != 0 else m[1] - 1
        else:
            ans = 1

        # 3. 중복 계산을 막기 위해 nums 대신 딕셔너리의 key(m)를 순회
        for c in m:
            if c == 1:
                continue
            
            chk = 0
            check = c
            
            # KeyExist 체크(check in m)를 항상 먼저 해주어야 KeyError를 방지합니다.
            while check in m and m[check] >= 2:
                chk += 2
                check = check ** 2
            
            # 루프가 끝났을 때 마지막 check가 m에 1개라도 남아있다면 중심점(+1)
            # 아예 없다면 이전 숫자를 중심점으로 써야 하므로 쌍 하나를 깸 (-1)
            if check in m and m[check] >= 1:
                chk += 1
            else:
                chk -= 1
            
            # 매번 최댓값을 정답 변수에 바로 갱신 (메모리 절약)
            ans = max(ans, chk)
            
        return ans