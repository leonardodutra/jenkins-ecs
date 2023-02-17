#!groovy
import jenkins.model.*
import hudson.model.*

def jenkinsInstance = Jenkins.getInstance()

def gitDescriptor = jenkinsInstance.getDescriptor('hudson.plugins.git.GitSCM')

gitDescriptor.setGlobalConfigName('jenkins-ci')
gitDescriptor.setGlobalConfigEmail('jenkins-ci@totalexpress.com.br')

gitDescriptor.save()
