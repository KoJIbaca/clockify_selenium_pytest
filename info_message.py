

class Message():

    def auth_message(func, text):
        if func.is_displayed() is True:
            print(f'{text} прошла успешно')
            assert True
        else:
            print(f'{text} не пройдена')
            assert False


    def drop_menu(func, text):
        if func.is_displayed() is True:
            print(f'{text} отображается')
            assert True
        else:
            print(f'{text} не отображается')
            assert False


    def profile_settings(func):
        if func.is_displayed() is True:
            print('Страница изменения профиля открыта')
            assert True
        else:
            print('Страница изменения профиля не открыта')
            assert False

    def name_change (func):
        if func.get_attribute('value') == 'Helicopter':
            print('Имя успешно изменено')
            assert True
        else:
            print('Произошла ошибка при изменении имени')
            assert False
