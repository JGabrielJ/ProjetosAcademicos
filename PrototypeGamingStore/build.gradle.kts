buildscript {
    repositories {
        google()
        mavenCentral()
    }
    dependencies {
        classpath(Config.Dependencies.androidPlugin)
        classpath(Config.Dependencies.kotlinPlugin)
        classpath(Config.Dependencies.googlePlugin)
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.8.0")
    }
}

allprojects {
    repositories {
        google()
        mavenCentral()
        maven { url = uri(Config.Repositories.jitPack) }
        maven { url = uri(Config.Repositories.pluginGradle) }
    }
}

tasks.register("clean",Delete::class){ delete(rootProject.buildDir) }