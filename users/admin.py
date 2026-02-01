from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser,Residente, Employee

# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin): #deixe o UserAdmin para garatir que fique seguro
#     list_display = (
#         'id',
#         'email', 
#         'username', )

#     list_filter = (
#         'id',
#         'email', 
#         'cpf',
#         'first_name',
#         'last_name')

#     #Página de edição caso o user já exista
#     fieldsets = UserAdmin.fieldsets + (
#     ('Information Users', {'fields': ('cpf','password_gate')}),
#     )

#     #Página de criação
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         ('Information Users', {'fields': ('cpf','password_gate','email')}),
#     )

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name','username', 'department','is_active')

    fieldsets = (
        ('Dados Principais', {
            'fields': (
                ('first_name', 'last_name'),
                'username',
                ('cpf', 'email'),
                 'department',           
            )
        }),
        ('Segurança', {
            'fields': (
                ('password'),
                ('gate_password')
            ),
        }),
          ('Dados Secundários',{
               'fields':(
                  ('is_active'),
              )}) 
    )



@admin.register(Residente)
class ResidentAdmin(admin.ModelAdmin):
    list_display = ('first_name','username','is_active')

    fieldsets = (
        ('Dados Principais', {
            'fields': (
                ('first_name', 'last_name'),
                'username',
                ('cpf', 'email'),
                ('floor_number','house_number'),           
            )
        }),
        ('Segurança', {
            'fields': (
                ('password'),
                ('gate_password') 
            ),
           # 'classes':('collapse',)
        }),
          ('Dados Secundários',{
               'fields':(
                  ('is_active'),
              )}) 
    )