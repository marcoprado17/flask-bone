var gulp = require("gulp");
var print = require("gulp-print");
var sass = require("gulp-sass");
var concat = require("gulp-concat");
var shell = require("gulp-shell");

gulp.task("watch", function () {
    gulp.watch("src/**/*.scss", ["make_css_bundle"]);
    gulp.watch("src/**/*.js", ["make_js_bundle"]);
    gulp.watch("src/**/*.html", ["refresh_page"]);
    gulp.watch("static/**/*.*", ["refresh_page"]);
});

gulp.task("make_css_bundle", function () {
    gulp.src(["bower_components/bootstrap/dist/css/bootstrap.css", "src/**/*.scss"])
        .pipe(sass())
        .pipe(concat("bundle.css"))
        .pipe(gulp.dest("static/css"));
});

gulp.task("make_js_bundle", function () {
    gulp.src(["bower_components/jquery/dist/jquery.js", "bower_components/bootstrap/dist/js/bootstrap.js", "src/**/*.js"])
        .pipe(concat("bundle.js"))
        .pipe(gulp.dest("static/js"));
});

gulp.task("refresh_page", shell.task([
    "./scripts/utils/refresh_page.sh"
]));