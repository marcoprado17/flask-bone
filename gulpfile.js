var gulp = require("gulp");
var print = require("gulp-print");
var sass = require('gulp-sass');
var concatCss = require('gulp-concat-css');

gulp.task('watch', function(){
  gulp.watch("src/**/*.scss", ['make_css_bundle']);
});

gulp.task("make_css_bundle", function () {
    gulp.src(["bower_components/bootstrap/dist/css/bootstrap.css", "src/**/*.scss"])
        .pipe(sass())
        .pipe(concatCss("bundle.css"))
        .pipe(gulp.dest("build/static/css"));
});