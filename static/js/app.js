/**
 * Created by geekaia on 19/03/17.
 */

var app = angular.module('capsapp', ['ngMaterial', 'ngRoute', 'ngMessages']);
app.controller('login', function($scope, $http) {
    $scope.usuario= "";
    $scope.senha= "";

    $scope.url = '/login/';

    $scope.logar  = function()
    {
        $scope.data = {
            'usuario' : $scope.usuario,
            'senha': $scope.senha,

        };

        // CSRFTOKEN
        $http.defaults.xsrfCookieName = 'csrftoken';
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';

        $http({
            method: "POST",
            url: $scope.url,
            data: $scope.data
        }).then(function getRespOk(resp) {
            if (resp.data.resp ==1 ){
                alert("Tudo ocorreu OK")
            } else {
                alert("Ocorreu um erro na authenticação!");
            }
        }, function getRespErro(resp) {
            alert("Ocorreu um erro na conexão!!!");
        });
    }
});


app.controller('pacientectl', function($scope, $http) {
    $scope.pc = {};
    $scope.data = $scope.pc;

    $scope.url = '/cadastrapaciente/';

    $scope.pccad  = function()
    {
        

        // CSRFTOKEN
        $http.defaults.xsrfCookieName = 'csrftoken';
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';

        $http({
            method: "POST",
            url: $scope.url,
            data: $scope.data
        }).then(function getRespOk(resp) {
            if (resp.data.resp ==1 ){
                alert("Tudo ocorreu OK")
            } else {
                alert("Ocorreu um erro na authenticação!");
            }
        }, function getRespErro(resp) {
            alert("Ocorreu um erro na conexão!!!");
        });
    }
});





app.config(function($routeProvider) {
   $routeProvider
       // .when("/", {
       //     templateUrl: "/"
       // })
       .when("/loginform", {
           templateUrl: "loginform.htm"
       })
       .when("/pacientecad", {
           templateUrl: "pacientecad.htm"
       });



});


app.controller('AppCtrl', function ($scope, $timeout, $mdSidenav) {
    $scope.toggleLeft = buildToggler('left');
    $scope.toggleRight = buildToggler('right');

    function buildToggler(componentId) {
      return function() {
        $mdSidenav(componentId).toggle();
      };
    }
  });

