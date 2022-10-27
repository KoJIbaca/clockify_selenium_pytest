

class messages():

    def auth_message(func, text):
        if func.is_displayed() is True:
            print('{} прошла успешно'.format(text))
            assert True
        else:
            print('{} не пройдена'.format(text))
            assert False


    def drop_menu(func, text):
        if func.is_displayed() is True:
            print('{} отображается'.format(text))
            assert True
        else:
            print('{} не отображается'.format(text))
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
