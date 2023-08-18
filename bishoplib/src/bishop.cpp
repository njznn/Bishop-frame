#include <iostream>
#include <string>
#include <cmath>
#include "../../bishoplib/include/bishop.hpp"
#include <stdio.h>
#include <stdlib.h>
#include <fstream>



Bishop::Bishop(const MatrixXd  &tocke_, Vector3d initvec,int st_tock_ ): X(initvec),st_tock(st_tock_),
  tocke(tocke_), T(MatrixXd::Zero(3, st_tock_-1)),V(MatrixXd::Zero(3, st_tock_-1)),
  N(MatrixXd::Zero(3, st_tock_-1)) {

    //tangentni vektorji:
    T(all,0) = (tocke(all, 1)-tocke(all, 0)) / (tocke(all, 1)-tocke(all, 0)).norm();
    for (size_t i = 1; i < (st_tock-1); i++) {
      T(all, i) = (tocke(all, i+1) - tocke(all, i-1))/(tocke(all, i+1) - tocke(all, i-1)).norm();
    }

    X = initvec;

    V(all, 0) = T(all, 0).cross(X);
    if (V(all, 0).dot(T(all, 0)) != 0.){
      std::cout << "Wrong Bishop frame, CHANGE RANDOM VECTOR." << '\n';
      exit(1);
    }

    for (size_t i = 0; i < (st_tock-2); i++) {
      B = T(all, i).cross(T(all, i+1));
      if (B.norm() == 0){
        V(all, i+1) = V(all, i);
      }
      else {
        B = B/(B.norm());
        double theta = acos(T(all, i).dot(T(all, i+1)));
        Quaterniond rot;
        rot.vec() = B*sin(theta/2);
        rot.w()= cos(theta/2);
        rot.normalize();
        Quaterniond p;
        p.vec() = V(all, i);
        p.w() = 0;
        Quaterniond rotatedP = rot* p * (rot.inverse());
        V(all, i+1) = rotatedP.vec();

      }
    }

    for (size_t i = 0; i < (st_tock-1); i++) {
      N(all, i) = T(all, i).cross(V(all, i));

    }



  }

Bishop::~Bishop(){};


void Bishop::draw(int everyNplot){
  std::ofstream outdata;
  outdata.open("T.txt", std::ofstream::out | std::ofstream::trunc);
  for (size_t i = 0; i < T.cols(); i++) {
    outdata << tocke.transpose()(i, all) << " "<< T.transpose()(i, all) << '\n';
  }
  outdata.close();
  outdata.open("tocke.txt", std::ofstream::out | std::ofstream::trunc);
  for (size_t i = 0; i < tocke.cols(); i++) {
    outdata << tocke.transpose()(i, all) << '\n';
  }
  outdata.close();
  outdata.open("V.txt", std::ofstream::out | std::ofstream::trunc);
  for (size_t i = 0; i < V.cols(); i++) {
    outdata << tocke.transpose()(i, all)<< " "<< V.transpose()(i, all) << '\n';
  }
  outdata.close();

  outdata.open("N.txt", std::ofstream::out | std::ofstream::trunc);
  for (size_t i = 0; i < N.cols(); i++) {
    outdata << tocke.transpose()(i, all)<< " "<< N.transpose()(i, all) << '\n';
  }
  outdata.close();

  


  FILE *gnuplot_fd;

                         // open pipe for writing
  if ( ( gnuplot_fd = popen( "gnuplot -p", "w" ) ) == NULL )
     {
       fprintf( stderr, "Error opening pipe to gnuplot\n" );
       exit(1);
     }


     //fprintf(gnuplot_fd, "set terminal png\n");
     //fprintf(gnuplot_fd, "set output 'bishop_helix_4.png'\n");
     //fprintf( gnuplot_fd, "set title \'Bishop frame of circular helix\'\n" );
     fprintf( gnuplot_fd, "unset key\n" );
     fprintf( gnuplot_fd, "set pointsize 0.5\n" );
     fprintf( gnuplot_fd, "set view equal xyz\n" );
     std::string strcom = "splot \'T.txt\' every ";
     strcom.append(std::to_string(everyNplot));
     strcom.append(" with vectors, \'tocke.txt\' w l, \'V.txt\' every ");
     strcom.append(std::to_string(everyNplot));
     strcom.append("with vectors,\'N.txt\' every ");
     strcom.append(std::to_string(everyNplot));
     strcom.append("with vectors  \n");

     
     const char* str = strcom.c_str();


     //fprintf( gnuplot_fd, "set xrange [-3:3]\n" );
     //fprintf( gnuplot_fd, "set yrange [-10:10]\n" );
     //fprintf( gnuplot_fd, "set zrange [0:8]\n" );
     fprintf( gnuplot_fd, str );
     fflush( gnuplot_fd );

  fprintf( gnuplot_fd, "exit\n" );
  pclose( gnuplot_fd );

}

MatrixXd Bishop::get_data(){
  MatrixXd outmat(3, int(4*(st_tock-1)+1)); // LAST last point has not triad!
  int k=0;
  for (size_t i = 0; i < (st_tock-1); i++)
  {
    k = 4*i;
    outmat(all, k) = tocke(all, i);
    outmat(all, k+1) = T(all, i);
    outmat(all, k+2) = V(all,i);
    outmat(all, k+3) = N(all, i);
  }
  outmat(all, 4*st_tock-4)=tocke(all, last);
  
  return outmat;

}



void Bishop::ortogonalcheck(double error){
  for (size_t i = 0; i < T.cols(); i++) {

    if (abs(T(all, i).dot(V(all, i))) > error){
      std::cout << "Vector T and d_ are not perpendicular to precision " + std::to_string(error) << '\n';
      break;
    }
    if (i == (T.cols()-1)){
      std::cout << "OK, vectors T and d_ are perpendicular to precision" + std::to_string(error) << '\n';
    }
  }
}

MatrixXd convtoeig(double * arrmat, int st_tock){
  MatrixXd mat(3,(st_tock-1)+1);
  
  for (int k = 0; k < 3*((st_tock-1)+1); k++){
    int j = k / 3;
    int i = k % 3;
    mat(i,j) = arrmat[k]; 
  }
  return mat;
}

double * eigtoptr(MatrixXd &mat){
  int st_tock = mat.cols();
  double* arr = new double[st_tock*3];
  for (int j = 0; j < st_tock; j++){
    for (int i = 0; i < 3; i++){
      arr[i+j*3] = mat(i,j);
    }
  }
  return arr;
}

void deleteptr( double *ptr){
  delete [] ptr; //freed memory
  ptr = NULL;
}

double * run(double * arrmat, double *init , int st_tock){
    MatrixXd tocke = convtoeig(arrmat, st_tock);
    Vector3d initvec;
    initvec(0) = init[0];
    initvec(1) = init[1];
    initvec(2) = init[2];
    Bishop bis1(tocke,initvec, st_tock);
    bis1.ortogonalcheck(pow(10, -6));
    MatrixXd mat = bis1.get_data();
    
    arrmat = eigtoptr(mat);
    
    return arrmat;
}

