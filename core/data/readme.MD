book_3.pkl: set, 리뷰가 3개 이상인 책들, GNN을 통한 추천에 사용 (추천 후보)

user_1.pkl: set, 리뷰가 1개 이상인 유저, GNN을 통한 추천에 사용

user_3_records.pkl: dict, 리뷰를 3개 이상 쓴 유저들의 책 기록. 코사인 유사도 계산에 사용

gnn_book.pkl: dict, 책의 아이디와 임베딩

gnn_user.pkl: dict, 유저의 아이디와 임베딩