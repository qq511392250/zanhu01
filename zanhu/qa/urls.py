from django.urls import path

from zanhu.qa import views

app_name = "qa"
urlpatterns = [
    path("", views.UnAnsweredQuestionListView.as_view(), name="unanswered_q"),
    path("answered/", views.AnsweredQuestionListView.as_view(), name="answered_q"),
    path("indexed/", views.QuestionListView.as_view(), name="all_q"),
    path("ask-question/", views.QuestionCreateView.as_view(), name="ask_question"),
    path("question-detail/<int:pk>", views.QuestionDetailView.as_view(), name="question_detail"),
    path("propose-answer/<int:question_id>", views.AnswerCreateView.as_view(), name="propose_answer"),
    path("question/vote/", views.question_vote, name="question_vote"),
    path("answer/vote/", views.answer_vote, name="answer_vote"),
    path("accept-answer/", views.accept_answer, name="accept_answer"),

]
