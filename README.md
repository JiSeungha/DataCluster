## 지조있는 만남(소비데이터 기반 친구 매칭 시스템)
Data Clustering for participate in the Financial Data Contest 2022

# ~ 기대효과 ~ 

첫째, 실제 개인소비데이터를 기반으로 군집화하는 위 시스템 성격상 기존 매칭 시스템의 단점이었던 악용 범죄를 충분히 격감시킬 수 있습니다. 해당 악용사례들에 대한 두려움을 가지고 있었던 기존 비이용자들의 유입이 크게 증가하여 시스템 활성화에  것이라고 기대됩니다.

둘째, 위 시스템을 통해 집단으로부터 소외된 사람들이 감소할 수 있다고 기대됩니다. mz세대의 특성상 활발하게 본인을 뽐내고 잘 어울리는 사람들이 늘어난 것은 사실이지만, 그와 반대로 본인이 위축되어 숨게되고 사회에 어울리기 힘들어하는 사람들도 적지 않습니다. 저희가 만들고자 하는 시스템은 사회적으로 소외된 사람들에게 사회로 다시 돌아오게 되는 트리거로 작용할 것입니다. 큰 노력없이도 해당 시스템에 이용만 하면 그들과 유사한 선호를 가진 사람들을 찾을 수 있습니다. 또한, 그들의 재사회화는 사회 전반적으로 굉장히 좋은 영향을 미칠 것입니다.

셋째, 매칭 시장의 성장에 따라 데이터 거래소 역시 활성화 할 수 있습니다. 현재 채용 광고 시장 규모는 헤드헌팅·후불형 채용 등 매칭 상품을 포함하면 2조원 가량입니다. 다올투자증권은 연간 채용 인력과 수수료를 감안할 때 2025년 국내 시장 규모가 3조8000억원에 달할 것이라고 전망했습니다. 이처럼 커져가는 P2P 매칭 시스템 시장에 맞추어 데이터거래소 플랫폼 역시 활성화 될 수 있으리라 기대합니다.


# Pseudo
1. clustering을 통한 계층 분류
2. cos similarity 등의 유사도 측정을 바탕으로 새로운 데이터가 어느 그룹에 속하는 지 확인
3. 새로운 data를 추가하고 다시 clustering을 통해 계층 분류


# Implementation

Clustering
1. 모든 point에 대해 각 point에서 directly density reachable한 point들을 구하고, core인지 확인한다.
2. core가 아닌 경우, outlier로 mark한 후 다음 point를 탐색한다.
3. core인 경우, 새로운 cluster를 생성하여 현재 point와 directly density reachable한 point들을 추가한다.
4. 마찬가지로 cluster 자료구조(ex: stack, queue… etc)에서 하나씩 꺼내어 directly density reachable한 point들을 추가하는 것을 반복한다.
5. set이 empty한 경우 cluster가 완성되었다는 의미이므로, 새로운 cluster를 추가한다.
6. cluster중 하나로 배정받지 못한 임의의 point에 대해 1번부터 반복한다.
7. clustering을 마치고 각 cluster들에 대해 small sizes in ascending order로 정렬한 후, 입력으로 주어진 cluster의 개수 n에 맞추어 제거한다.
8. cluster내부 point들을 ID 순서에 맞추어 정렬한 후, output file을 생성한다.
