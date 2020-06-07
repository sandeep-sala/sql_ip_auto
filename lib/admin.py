import urllib.request
import urllib.error
import threading


url = ''


def find():
    file = open('Admins.txt', "w")
    file.write("\n:::     Possible Admin Found     :::\n")

    def scan(links):
        for x in links:
            curl = url + x
            try:
                openurl = urllib.request.urlopen(curl)
                file.write(curl + "\n")

            except urllib.error.URLError as msg:
                print("[No Admin] " + curl)

    paths1 = ['admin/', 'administrator/', 'admin1/', 'admin2/', 'admin3/', 'admin4/', 'admin5/', 'usuarios/',
              'usuario/',
              'administrator/', 'moderator/', 'webadmin/', 'adminarea/', 'bb-admin/', 'adminLogin/', 'admin_area/',
              'panel-administracion/', 'instadmin/',
              'memberadmin/', 'administratorlogin/', 'adm/', 'admin/account.php', 'admin/index.php', 'admin/login.php',
              'admin/admin.php', 'admin/account.php',
              'admin_area/admin.php', 'admin_area/login.php', 'siteadmin/login.php', 'siteadmin/index.php',
              'siteadmin/login.html', 'admin/account.html', 'admin/index.html', 'admin/login.html', 'admin/admin.html',
              'admin_area/index.php', 'bb-admin/index.php', 'bb-admin/login.php', 'bb-admin/admin.php',
              'admin/home.php', ]
    paths3 = ['admin_area/login.html', 'admin_area/index.html',
              'admin/controlpanel.php', 'admin.php', 'admincp/index.asp', 'admincp/login.asp', 'admincp/index.html',
              'admin/account.html', 'adminpanel.html', 'webadmin.html',
              'webadmin/index.html', 'webadmin/admin.html', 'webadmin/login.html', 'admin/admin_login.html',
              'admin_login.html', 'panel-administracion/login.html',
              'admin/cp.php', 'cp.php', 'administrator/index.php', 'administrator/login.php', 'nsw/admin/login.php',
              'webadmin/login.php', 'admin/admin_login.php', 'admin_login.php',
              'administrator/account.php', 'administrator.php', 'admin_area/admin.html', 'pages/admin/admin-login.php',
              'admin/admin-login.php', 'admin-login.php', ]
    paths2 = ['bb-admin/index.html', 'bb-admin/login.html', 'acceso.php', 'bb-admin/admin.html', 'admin/home.html',
              'login.php', 'modelsearch/login.php', 'moderator.php', 'moderator/login.php',
              'moderator/admin.php', 'account.php', 'pages/admin/admin-login.html', 'admin/admin-login.html',
              'admin-login.html', 'controlpanel.php', 'admincontrol.php',
              'admin/adminLogin.html', 'adminLogin.html', 'admin/adminLogin.html', 'home.html',
              'rcjakar/admin/login.php',
              'adminarea/index.html', 'adminarea/admin.html',
              'webadmin.php', 'webadmin/index.php', 'webadmin/admin.php', 'admin/controlpanel.html', 'admin.html',
              'admin/cp.html', 'cp.html', ]
    paths4 = ['wp-login.php', 'adminLogin.php', 'admin/adminLogin.php', 'home.php',
              'admin.php', 'adminarea/index.php',
              'adminarea/admin.php', 'adminarea/login.php', 'panel-administracion/index.php',
              'panel-administracion/admin.php', 'modelsearch/index.php',
              'modelsearch/admin.php', 'admincontrol/login.php', 'adm/admloginuser.php', 'admloginuser.php',
              'admin2.php',
              'admin2/login.php', 'admin2/index.php', 'usuarios/login.php',
              'adm/index.php', 'adm.php', 'affiliate.php', 'adm_auth.php', 'memberadmin.php', 'administratorlogin.php']
    paths5 = ['adminpanel.php', 'moderator.html',
              'administrator/index.html', 'administrator/login.html', 'user.html', 'administrator/account.html',
              'administrator.html', 'login.html', 'modelsearch/login.html',
              'moderator/login.html', 'adminarea/login.html', 'panel-administracion/index.html',
              'panel-administracion/admin.html', 'modelsearch/index.html', 'modelsearch/admin.html',
              'admincontrol/login.html', 'adm/index.html', 'adm.html', 'moderator/admin.html', 'user.php',
              'account.html',
              'controlpanel.html', 'admincontrol.html',
              'panel-administracion/login.php', ]

    def part1():
        links = paths1  # it is the first part of the list
        scan(links)  # calls the scanner

    def part2():
        links = paths2  # it is the second part of the list
        scan(links)  # calls the scanner

    def part3():
        links = paths3  # it is the first part of the list
        scan(links)  # calls the scanner

    def part4():
        links = paths4  # it is the first part of the list
        scan(links)  # calls the scanner

    def part5():
        links = paths5  # it is the first part of the list
        scan(links)  # calls the scanner

    t1 = threading.Thread(target=part1)  # Calls the part1 function via a thread
    t2 = threading.Thread(target=part2)  # Calls the part2 function via a thread
    t3 = threading.Thread(target=part3)
    t4 = threading.Thread(target=part4)
    t5 = threading.Thread(target=part5)
    t1.start()  # starts thread 1
    t2.start()  # starts thread 2
    t3.start()
    t4.start()
    t5.start()
    t1.join()  # Joins both
    t2.join()  # of the threads
    t3.join()
    t4.join()
    t5.join()
