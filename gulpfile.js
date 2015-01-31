"use strict";
var gulp = require('gulp'),
    uglify = require('gulp-uglify'),
    concat = require('gulp-concat'),
    hash = require('gulp-hash'),
    less = require('gulp-less'),
    LessPluginCleanCSS = require("less-plugin-clean-css"),
    cleancss = new LessPluginCleanCSS({advanced: true});

gulp.task('scripts', function () {
    return gulp.src([
        'static/js/vendor/lodash.min.js',
        'static/js/vendor/angular.min.js',
        'static/js/vendor/angular-ui-router.min.js',
        'static/js/vendor/restangular.min.js',
        'static/js/vendor/ui-bootstrap-tpls-0.12.0.min.js',
        'static/js/app/app.js',
        'static/js/app/controllers.js'
    ])
        .pipe(uglify())
        .pipe(concat('scripts.js'))
        .pipe(gulp.dest('dist'));
});

gulp.task('style', function () {
    return gulp.src('static/style/main.less')
        .pipe(less({
            plugins: [cleancss]
        }))
        .pipe(gulp.dest('dist'));
});

gulp.task('default', ['scripts', 'style']);
