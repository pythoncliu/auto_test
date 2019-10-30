from jenkinsapi.jenkins import Jenkins

JENKINS_RA_FOLDER_URL = "http://192.168.17.139:8080/"
jenkins_server_obj = Jenkins(JENKINS_RA_FOLDER_URL, username='jason', password='123456', lazy=True, ssl_verify=False)
JENKINS_INSTALLER_JOB_NAME = "selenium"

#start a job
jenkins_server_obj.build_job(JENKINS_INSTALLER_JOB_NAME)
jenkins_job_instance = jenkins_server_obj.get_job(JENKINS_INSTALLER_JOB_NAME)

#get job list
print(jenkins_server_obj.get_jobs_list())
#get job selenium 
print(jenkins_job_instance)
#global message
jenkins_server_obj.pprint()
#job config.xml
xml = jenkins_server_obj['selenium'].get_config()
print(xml)
'''
#CURB JOB
jenkins_server_obj.create_job('RF1',xml)
jenkins_server_obj.delete_job('RF1')
jenkins_server_obj.copy_job('selenium','selenium3')
jenkins_server_obj.rename_job('selenium1','selenium4')
'''
#job list
jobs = jenkins_server_obj.get_jobs()
for job in jobs:
    print(job[0])

#get plugin details
for plugin in jenkins_server_obj.get_plugins().values():
    print('-------------------------------------------------------------')
    print(plugin)
    #print("short name:%s" % (plugin.shortname))
    #print("long name:%s" % (plugin.longname))
    print("version:%s" % (plugin.version))
    print("url:%s" % (plugin.url))
    print("active:%s" % (plugin.active))
    #print("enabled:%s" % (plugin.enable))

print(jenkins_server_obj.has_job('RF3'))
print(jenkins_server_obj.has_job('RF2'))
print(jenkins_server_obj.get_queue())
#check view
print(jenkins_server_obj.views.keys())
#get the last build
print(jenkins_server_obj['selenium'].get_last_good_build())
