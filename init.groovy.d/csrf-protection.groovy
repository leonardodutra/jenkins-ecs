#!groovy

// imports
import java.util.logging.Logger
import jenkins.model.Jenkins
import hudson.security.csrf.DefaultCrumbIssuer

// get Jenkins instance
Jenkins jenkins = Jenkins.getInstance()
Logger logger = Logger.getLogger("dsuite/jenkins")

logger.info("enabling slave master access control")

// set default crumb issuer
jenkins.setCrumbIssuer(new DefaultCrumbIssuer(true))

// save current Jenkins state to disk
jenkins.save()
