/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package kinematics;

public class Ball {

    private double x;
    private double y;
    public double xVel;
    public double yVel;

    private int width;
    private int height;

    private static final int dWidth = 10;
    private static final int dHeight = 10;

    public Ball(int x, int y, int xVel, int yVel, int width, int height) {
        this.x = x;
        this.y = y;
        this.xVel = xVel;
        this.yVel = yVel;
        this.width = width;
        this.height = height;
    }

    public Ball(int x, int y, int xVel, int yVel) {
        this.x = x;
        this.y = y;
        this.xVel = xVel;
        this.yVel = yVel;
        this.width = dWidth;
        this.height = dHeight;
    }

    public void update() {
        this.x += xVel;
        this.y += yVel;
    }

    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }

    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }

    public double getX() {
        return x;
    }

    public void setX(double x) {
        this.x = x;
    }

    public double getxVel() {
        return xVel;
    }

    public void setxVel(double xVel) {
        this.xVel = xVel;
    }

    public double getY() {
        return y;
    }

    public void setY(double y) {
        this.y = y;
    }

    public double getyVel() {
        return yVel;
    }

    public void setyVel(double yVel) {
        this.yVel = yVel;
    }
}
