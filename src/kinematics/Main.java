/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package kinematics;

import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Timer;
import java.util.TimerTask;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class Main extends JPanel {

    private static final long serialVersionUID = 1L;
    private static final int maxBalls = 250;
    int currentNumBalls = 0;
    private static Ball[] balls = new Ball[maxBalls];

    private static final int fps = 50;
    private static final int ms = 1000 / fps;
    public int loop = 0;
    public int time = 0;

    private static final double mass = 1;

    private static final double a = 1.1;//gravitational force
    private static final double CoR = 0.8;//restitution
    private static final double CoF = 0.9;//friction
    private static Timer animationTimer;
    private static TimerTask animationTask;

    public Main() {
        for (int i = 0; i < maxBalls; i++) {
            balls[i] = new Ball(20, 20, (int) ((Math.random() * 15)), (int) ((Math.random() * 15)), 25, 25);
        }
        animationTimer = new Timer("Ball Animation");
        animationTask = new updateAnimation();
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Kinematics Physics Engine");
        Main panel = new Main();
        frame.getContentPane().add(panel);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JButton restartButton = new JButton("reset");

        JPanel buttonPane = new JPanel();
        buttonPane.add(restartButton);

        frame.add(buttonPane, BorderLayout.NORTH);//Add the button to the JFrame.
        restartButton.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {
                animationTimer.cancel();
                animationTask.cancel();
                for (int i = 0; i < maxBalls; i++) {
                    balls[i] = null;
                }
                frame.getContentPane().invalidate();
                main(new String[]{"a", "b", "c"});
            }
        });

        frame.pack();
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
        panel.start();
    }

    public void start() {
        animationTimer.schedule(animationTask, 0, ms);
    }

    @Override
    public Dimension getPreferredSize() {
        return new Dimension(400, 400);
    }

    public void instantiate() {
        if (currentNumBalls < maxBalls) {
            balls[currentNumBalls].setX(20);// = 20;
            balls[currentNumBalls].setY(20);// = 20;
            balls[currentNumBalls].setxVel((int) ((Math.random() * 8)));//)= (int) ((Math.random()*8));
            balls[currentNumBalls].setyVel((int) ((Math.random() * 8)));//= (int) ((Math.random()*5));
        } else {
            System.out.println("unnable to comply");
        }
    }

    public void handleCollisions() {
        double xDist, yDist;
        for (int i = 0; i < balls.length; i++) {
            for (int j = i + 1; j < balls.length; j++) {
                xDist = balls[i].getX() - balls[j].getX();
                yDist = balls[i].getY() - balls[j].getY();
                double distSquared = xDist * xDist + yDist * yDist;

                if (distSquared <= ((balls[i].getWidth()) / 2 + (balls[j].getWidth()) / 2) * ((balls[i].getWidth()) / 2 + (balls[j].getWidth()) / 2)) {
                    double xVelocity = balls[j].xVel - balls[i].xVel;
                    double yVelocity = balls[j].yVel - balls[i].yVel;
                    double dotProduct = xDist * xVelocity + yDist * yVelocity;

                    if (dotProduct > 0) {
                        double collisionScale = dotProduct / distSquared;
                        double xCollision = xDist * collisionScale;
                        double yCollision = yDist * collisionScale;

                        double combinedMass = mass + mass;
                        double collisionWeightA = 2 * mass / combinedMass;
                        double collisionWeightB = 2 * mass / combinedMass;
                        balls[i].xVel += collisionWeightA * xCollision;
                        balls[i].yVel += collisionWeightA * yCollision;
                        balls[j].xVel -= collisionWeightB * xCollision;
                        balls[j].yVel -= collisionWeightB * yCollision;
                    }
                }
            }
        }
    }

    public void paintComponent(Graphics g) {
        super.paintComponent(g);

        g.clearRect(0, 0, getWidth(), getHeight());

        for (int i = 0; i < currentNumBalls; i++) {
            int upperLeftX = (int) (balls[i].getX() - balls[i].getWidth() / 2);
            int upperLeftY = (int) (balls[i].getY() - balls[i].getHeight() / 2);

            g.fillOval(upperLeftX, upperLeftY, balls[i].getWidth(), balls[i].getHeight());
        }
    }

    private class updateAnimation extends TimerTask {

        public void run() {
            for (int i = 0; i < currentNumBalls; i++) {
                double v2 = (a * 1) + balls[i].getyVel();

                balls[i].setyVel(v2);
                balls[i].update();

                handleCollisions();

                int maxY = getHeight() - (balls[0].getHeight() / 2);
                int maxX = getWidth() - (balls[0].getWidth() / 2);
                int minX = 0 + balls[0].getWidth() / 2;

                if (balls[i].getY() > maxY) {
                    balls[i].setY(maxY);
                    balls[i].setyVel(-CoR * balls[i].getyVel());
                } else if (balls[0].getY() < 0) {
                    balls[i].setY(0);
                    balls[i].setyVel(-CoR * balls[i].getyVel());
                }

                if (balls[i].getX() > maxX) {
                    balls[i].setX(maxX);
                    balls[i].setxVel(-CoR * balls[i].getxVel());
                } else if (balls[i].getX() < minX) {
                    balls[i].setX(minX);
                    balls[i].setxVel(-CoR * balls[i].getxVel());
                }

                if (balls[i].getY() == maxY) {
                    balls[i].setxVel(CoF * balls[i].getxVel());
                }

                repaint();
            }

            loop++;
            if (loop % 30 == 0) {
                time = loop / 30;

                if (time % 1 == 0 && currentNumBalls < maxBalls) {
                    instantiate();
                    currentNumBalls += 1;
                }
            }
        }
    }
}
