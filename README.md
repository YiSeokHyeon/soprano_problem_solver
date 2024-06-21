# soprano_problem_solver 작곡을 수학만큼이나 중요하게 다루고 있는 나로서는, 작곡의 행위에 있어서 어디까지가 ‘계산될 수 있는 영역’인가가 나의 관심중 하나이다. 수학적으로 이야기 하자면, 작곡의 irreduciblity를 실험하고 알고 싶은 것이다. 화성학은 모든 작곡과에서 기본소양으로서 다루어지고 있다. 거의 모든 화성학의 실습은 주어진 소프라노 또는 베이스 4성부 작곡으로 진행되는데, 이때 화성학에서는  ‘쓰면 안되는 진행’을 명시하고, 학생은 이 ‘규칙’을 잘 지켜서 4성부를 완성해야만 한다. 즉, 음악에 일종에 ‘금칙’을 정하고 있다는 점에서 꽤나 흥미로운 지점인데, 처음 접하는 입장에서 이 규칙들을 지키면서도 음악적으로 답안을 작성하는것은 꽤나 많이 어렵다.
예시를 들어보겠다.

![KakaoTalk_Photo_2024-06-21-11-15-39 002](https://github.com/YiSeokHyeon/soprano_problem_solver/assets/171541916/202cd3d9-d9ab-4531-9229-ddfa25bc403e)


중간에 동그라미4번이 문제이고, 아래에 있는 숫자들은 어떤 화음이 오는지를 나타내는 숫자들이다.
이것의 풀이는 다음과 같다. 

![KakaoTalk_Photo_2024-06-21-11-15-39 001](https://github.com/YiSeokHyeon/soprano_problem_solver/assets/171541916/1ffc4dbe-0dff-4b5d-9ac8-4aabe62263db)
 
 이 문제를 푸는 것이 생각보다 어려운 것은 한 음을 적어도 꽤나 많은 제약이 따르기 때문이다. 다음은 대표적인 규칙들이다. 세세하게 들어가면 이것보다 배로 많다. 화성학 교재에도 여러가지가 있는데, 내가 선택한 교재는 우리나라에서 보편적으로 사용되는 백병동 화성학임을 밝혀둔다.

성부별 음역을 지켜야만 한다.
상3성의 인접한 두개의 성부의 간격이 옥타브를 넘어가면 안된다.
병행, 은복 1 5 8 금지.
성부침해 금지.
증음정 진행 금지.
대사현상 금지.
주3,부3화음의 2전위의 사용은 베이스 순차진행, 공통음진행, 분산화음적 진행, 종지적 진행 이외에는 금한다.
7음은 항상 예비와 해결이 있어야만 한다. 
반음계적 변화음들도 예비와 해결이 있어야만 한다. 

 그래서 나는 이런 규칙에 의한 “음을 쓰기”에 알고리즘과 AI로의 활용가능성을 보았다. 전세계적으로 봐도 나와 같은 시도를 한 사람들은 손에 꼽고, 특히 내가 이번에 시도한 화성학 문제풀이 프로그램은 시중에 나온것이 전무하다. 여기서 이 4성부 문제 풀이의 중요성을 언급하자면, 이 4성부의 구조가 기본이 되어 정말 많은 작품들(대표적으로 교향곡)이 나왔고, 현대음악작곡가에게도 곡을 쓸때 정말 기본이 되는 소양이다.

 정확히 이번 프로젝트의 주제를 명확히 이야기 해보겠다. 이 4성부 문제에는 3가지 유형의 문제가 있는데, 그중에 나는 가장 어려운 소프라노 문제를 푸는 프로그램을 다뤘다. 나는 이 문제풀이 프로그램을 알고리즘파트와 딥러닝파트 이렇게 2가지로 나누려고 한다. 내가 이번에 제출하는 것은 알고리즘 파트이다. 아직 완성을 못했고, 이는 어디까지를 확실한 알고리즘(규칙)으로 볼것인지도 애매하고, 이 구현방식이 향후 딥러닝과 연관시키기 위해 최소한의, 하지만 충분한 규칙으로 구현을 해야 하며, 무엇보다 이 알고리즘을 구현하는 자체도 복잡하며 정말 간단한 것부터 다 만들어야 하기에 정말 큰 에너지가 소모되기에 적어도 1년이 필요하다. 나는 이것을 적어도 4년 이상 연구하고 나중에는 음악교육에 활용될 수 있도록 개발할 생각이다.

 내가 사용한 라이브러리는 music21이라는 파이썬 라이브러리이다. MIT에서 만들었고, 음악학과 음악교육, 작곡에 도움이 되기 위한 목적으로 만든 라이브러리이다. 전체적인 작동방식은 사용자가 소프라노 문제를 담은 미디파일을 .py에 같은 디렉토리에 놓으면, 코드를 실행하여 알고리즘의 결과값들을 얻어서 이것을 4성부가 다 채워진 미디파일로 export하여 사용자가 사보 프로그램으로 문제풀이를 확인하는 방식이다. 유저 인터페이스의 개발도 필요하지만, 이는 여기서 언급하지 않겠다.

 내가 구현한 것은 100퍼센트 알고리즘이기에 코드를 직접 보면서 주석을 잘 읽어보길 권장한다. 주석과 변수를 정말 직관적으로 이해할 수 있도록 노력했다.

여기서는 어떤 알고리즘이 쓰였는지 쭉 과정 순서로 정리를 해보겠다. 여기서 숫자들은 소스코드 안의 주석의 단계번호와 같다. 메인 소스코드는 main1.py이다.

0. 송출할때 필요한 사보프로그램을 sibelius로 정한다.
텅 빈 악보를 하나 만든다.
여기에 4성부를 정의하고 이름을 붙인다.
각각에 맞는 음자리표를 입력한다.
문제를 불러온다. 소프라노 문제이기에 개별 음들의 음가와 음고 뿐만이 아니라, 조표와 박자표까지 얻어야 한다. 그것을 함수 2개로  구현했다.
문제에 맞는 조표를 전 성부에 입력한다.
박자표 역시 전 성부에 입력한다.
그리고 소프라노는 주어졌으므로, 입력된 미디정보를 그대로 소프라노에 입력한다.
소프라노의 음가를 단위박으로 다 쪼갠다. 이렇게 하는 이유는 화성이 변하는 단위를 단위박으로 쪼개기 위함이다.
소프라노의 음가를 단위박으로 쪼갰으면, 각각의 소프라노 음들의 음도(scale degree)를 계산한다.
 음도를 구했다면, 여기에 쓸 수 있는 기본적인 화음이 4개로 제한되는데 그 화성들은 Z7의 modulo addition으로 구할수 있다. 즉 소프라노의 음도가 2면, 코드에 주어진 바와 같이 2, 2-2, 2-4, 2-6의 화음을 쓸 수 있다. 화성학으로 이야기 하자면, 주어진 소프라노의 음을 어떤 화성의 근음으로 볼것인지, 3음으로, 5음으로, 7음으로 볼것인지를 생각하는 것과 equivalent하다.
 8개의 규칙을 만족하는 화성을 고른다. 단위박으로 쪼개진 소프라노에 대해서 각각의 단위박에서 4개의 기본화음의 전위도 생각해야 하나, 그 전에 정말 기본적으로 하면 안되는 것들을 먼저 거르고 시작하기 위해 이 단계를 만들었다. 8개의 규칙은 소스코드 안의 주석에 설명이 되어있으나, 사실 병행 1,5,8도과 은복1,5,8,까지 포함하여 기본 규칙은 10개 이상으로 구성되어있어야만 한다. 그런데 이미 8개만 가지고도 복잡해지고 있으니, 좀더 쉬운 방식으로 함수를 정의해야 할것 같다.
각 성부에는 음역제한이 있다. 성부의 음역을 표현하기 위한 코드를 구현했다. 플랫, 샵뿐만이 아니라, 향후 모든 반음계적인 진행들을 구현할때 용이하기 위해 더블샵과 더블플랫을 포함시겼다. 


이정도로 구성해보았다.


향후 해야 할것은, 최소한의 충분한 제한알고리즘을 구현을 하는 것이고, 딥러닝(transformer)을 통해 비화성음과 같은 실제 음악적인 요소들을 충분히 출력하도록 학습을 시키고, 유저 인터페이스를 만드는 것이다. 결론적으로는 맨 위의 첫번째 사진에 보이는 문제를 미디파일로 입력을 하면 2번째 풀이처럼 유저가 볼수 있게 출력하는 것이 목표이다. 
