"use strict";

var TodoController = function ($scope, Restangular) {
    var items = Restangular.all('todo');
    $scope.todos = items.getList().$object;
};

TodoController.$inject =['$scope', 'Restangular'];

pmApp.controller('TodoController', TodoController);
