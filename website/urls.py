from django.contrib import admin
from django.urls import path, include
from website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.index, name = 'home'),
    path('aboutproject/', views.aboutproject, name ='aboutproject'),
    path('problem-statement/', views.problem_statement, name ='problem_statement'),
    path('scope-of-the-project/', views.scope_project, name ='scope_project'),
    
    path('Reg-Form-House-Wife', views.reg_form_house_wife, name ='reg-form-house-wife'),
    path('Reg-Form-Company/', views.reg_form_company, name = 'reg-form-company'),
            
    path('login', views.login_user, name ='login'),
    
    path('dashboard/', views.dashboard, name ='dashboard'),
    path('logout', views.logout_user, name ='logout'),
    path('info/', views.enquiry_info, name ='enquiry_info'),
    path('delete/<int:id>/', views.delete_record, name ='delete_record'),
    path('edit/<int:id>/', views.edit_record, name ='edit_record'),
    path('update/<int:id>/', views.update_record, name ='update_record'),
    path('student_data', views.student_data.as_view(), name ='student_data'),
    # path('student_data', views.student_data, name ='student_data'),

]