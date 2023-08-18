#ifndef BISHOP_HPP
#define  BISHOP_HPP
#include <iostream>

#include <string>
#include <cmath>
#include <Eigen/Dense>
#include <fstream>
using namespace Eigen;



class Bishop {
  public:
    int st_tock;
    const MatrixXd &tocke;
    Matrix<double, 3, Dynamic> T; //tangentni vektorji
    Matrix<double, 3, Dynamic> V;
    Vector3d X;
    Matrix<double, 3, Dynamic> N;
    Vector3d B; //binormalni vektor med točkama


  Bishop(const MatrixXd &tocke_ ,Vector3d initvec,int st_tock_);

  virtual ~Bishop();

  void draw(int everyNplot);

  MatrixXd get_data();

  void ortogonalcheck(double error);

};

extern "C"
{
double * run(double * tocke, double *arrvec, int st_tock);


MatrixXd convtoeig(double * arrmat,  int st_tock);

double * eigtoptr(MatrixXd &res);

void deleteptr( double *ptr);
}

#endif
