var btn = document.getElementById('submit');//버튼이 클릭 될 때(폼이 제출될 때 실행)

//할일(함수 필요)

btn.addEventListener('click', function(){
    //클릭후 할 일
    
    //어제 구현한 부분 넣기

    // name==group1인 거에서 가져온 값을 변수( home )에 저장

    // id=group1으로 새로 만들어준 코드 부분에 innerHTML로 값 넣기
    document.getElementById('group1').innerHTML = home;

});

// 선택결과를 저장한 코드 부분을 화면에서는 안보이게 처리
// 위에 코드부분을 form형태로 해서 default text로 처리해버려? 그래서 submit버튼 누를 때 {% url new %}이런 걸로 상세 정보 페이지 내용이 고쳐지게 해야하나?
// new함수에서 글 작성하면 상세정보페이지에 넘어가게 했던 것처럼 views.py를 만들어야하나??
