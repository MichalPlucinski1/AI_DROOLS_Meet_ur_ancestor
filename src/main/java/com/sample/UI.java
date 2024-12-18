package com.sample;

import org.kie.api.logger.*;
import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.concurrent.CompletableFuture;

import javax.imageio.ImageIO;

import org.kie.api.runtime.KieSession;


public class UI {
	
	JFrame frame;
	KieRuntimeLogger logger;
	
	public UI(JFrame frame, KieRuntimeLogger logger) {
		this.frame = frame;
		this.logger = logger;
	};
	
		
    // The initial screen (similar to your init function)
    public void initScreen(KieSession kSession) {
        this.frame.getContentPane().removeAll(); // Clear existing content

        JLabel background = new JLabel(new ImageIcon("src/main/resources/assets/init_screen.jpg"));
        background.setBounds(0, 0, 600, 800);
        this.frame.add(background);

        JButton button = new JButton("What the arrow says");
        button.setBounds(200, 600, 200, 100);
        background.setLayout(null);
        background.add(button);

        button.addActionListener(e -> {
            this.frame.getContentPane().removeAll();
            kSession.fireAllRules(); // Trigger the Drools rule engine
        });

        this.frame.setVisible(true);
    }
    
    public String questionScreen(String question, String... answers) {
        // Remove all previous components
        this.frame.getContentPane().removeAll();

        // Set a new layout with a vertical BoxLayout
        this.frame.setLayout(new BorderLayout());

        // Panel for the Question (at the top)
        JPanel questionPanel = new JPanel();
        questionPanel.setBackground(new Color(240, 240, 240)); // Light gray background
        JLabel questionLabel = new JLabel(question, SwingConstants.CENTER);
        questionLabel.setFont(new Font("Arial", Font.BOLD, 26));
        questionLabel.setForeground(new Color(50, 50, 50)); // Dark text color
        questionLabel.setBorder(BorderFactory.createEmptyBorder(100, 20, 100, 20));
        questionPanel.add(questionLabel);

        // Panel for the Answers (at the center)
        JPanel answersPanel = new JPanel();
        answersPanel.setLayout(new GridLayout(2, 0, 10, 10)); // Vertical grid layout with spacing
        answersPanel.setBorder(BorderFactory.createEmptyBorder(200, 20, 50, 20)); // Add padding
        answersPanel.setBackground(new Color(250, 250, 250)); // Slightly white background

        // Create a CompletableFuture to hold the user's choice
        String[] chosenAnswer = {"null"};
        
        // Dynamically create buttons based on the answers provided
        for (String answer : answers) {
            JButton answerButton = new JButton("<html><center>" + answer + "</center></html>");
            answerButton.setFont(new Font("Arial", Font.PLAIN, 10));
            answerButton.setBackground(new Color(100, 150, 255)); // Blue background
            answerButton.setForeground(Color.WHITE); // White text
            answerButton.setFocusPainted(false);
            answerButton.setBorderPainted(false);
            answerButton.setPreferredSize(new Dimension(200, 50));
            answerButton.setHorizontalAlignment(SwingConstants.CENTER); // Center align text
            answerButton.setVerticalAlignment(SwingConstants.CENTER);
            
            // Add action listener for the button (you can replace with custom behavior)
            answerButton.addActionListener(e -> {
                System.out.println("Selected: " + answer); // Debugging output
                chosenAnswer[0] = answer;
            });

            answersPanel.add(answerButton);
            
        }

        // Add panels to the frame
        this.frame.add(questionPanel, BorderLayout.NORTH);
        this.frame.add(answersPanel, BorderLayout.CENTER);

        // Refresh the frame
        this.frame.revalidate();
        this.frame.repaint();
        this.frame.setVisible(true);

        return chosenAnswer[0];
    };
    
    public static void resultScreen() {};
}

