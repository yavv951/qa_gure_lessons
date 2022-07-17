# qa_gure_lessons

Install allure
sudo apt-add-repository ppa:qameta/allure
sudo apt-get update 
sudo apt-get install allure

Если allure не запускается ,необходимо выполнить :
- Получить последнюю сборку deb

 wget https://github.com/allure-framework/allure2/releases/download/2.18.1/allure_2.18.1-1_all.deb

- Установите его с помощью dpkg

 sudo dpkg -i allure_2.18.1-1_all.deb