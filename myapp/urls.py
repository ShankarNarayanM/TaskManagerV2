from django.urls import path
from . import views
urlpatterns = [
    path('',views.landingPage,name="landingPage"),
    path('login',views.loginPage,name="loginPage"),
    path('register',views.registerPage,name="registerPage"),
    path('task-list',views.TaskList,name="taskListPage"),
    path('contact',views.contacts,name="contactPage"),
    path('dashboard',views.dashboard,name="dashboardPage"),
    path('logout',views.logout,name="logoutPage"),
    path('pricing',views.pricing,name="pricingPage"),
    path('forgot-password',views.forgotPassword,name="forgotPasswordPage"),
    path('reset-password/<uidb64>/<token>',views.resetPassword,name="resetPasswordPage"),
    path('add-task',views.addTask,name="addTaskPage"),
    path('edit-task/<int:task_id>',views.editTask,name="editTaskPage"),
    path('delete-task/<int:task_id>',views.deleteTask,name="deleteTaskPage"),
    path('my-profile/',views.myProfile,name="myProfilePage"),
]
