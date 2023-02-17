#!groovy
import jenkins.model.*
import hudson.model.*

// Jenkins global Maven configuration
def mavenConfig = Jenkins.getInstance().getExtensionList(hudson.tasks.Maven.DescriptorImpl.class)[0]
//M2_HOME has to be a global environment variable, can be replaced with any string
mavenConfig.setInstallations(new hudson.tasks.Maven.MavenInstallation('Maven', System.getenv('M2_HOME'), []))
mavenConfig.save()
