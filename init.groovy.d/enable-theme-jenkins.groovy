#!groovy

// imports
import java.util.logging.Logger
import jenkins.model.Jenkins

// get Jenkins instance
Jenkins jenkins = Jenkins.getInstance()
Logger logger = Logger.getLogger("dsuite/jenkins")

try {
    // Updated Theme
    def r = new Random()
    def ipAddress = InetAddress.localHost.hostAddress
    def colours = ['neo-light']
    def colour = colours.get(r.nextInt(colours.size()))

    def theme = jenkins.getDescriptorByType(org.codefirst.SimpleThemeDecorator.class)
    theme.setElements([new org.jenkinsci.plugins.simpletheme.CssUrlThemeElement("https://tobix.github.io/jenkins-neo2-theme/dist/${colour}.css")])
    jenkins.save()

    logger.info("Updating jenkins theme to: ${colour}")
} catch(Exception e) {

    logger.warning("styling failed")
    logger.warning("${e}")
}
