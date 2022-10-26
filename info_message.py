class messages():

    def auth_message(func, text):
        if func.is_displayed() is True:
            print('{} прошла успешно'.format(text))
        else:
            print('{} не пройдена'.format(text))
        return


    def drop_menu(func, text):
        if func.is_displayed() is True:
            print('{} отображается'.format(text))
        else:
            print('{} не отображается'.format(text))


    def profile_settings(func):
        if func.is_displayed() is True:
            print('Страница изменения профиля открыта')
        else:
            print('Страница изменения профиля не открыта')

    def name_change (func):
        if func.get_attribute('value') == 'Helicopter':
            print('Имя успешно изменено')
        else:
            print('Произошла ошибка при изменении имени')