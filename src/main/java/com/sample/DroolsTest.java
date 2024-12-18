package com.sample;

import org.kie.api.KieServices;
import org.kie.api.runtime.KieContainer;
import org.kie.api.runtime.KieSession;
import org.kie.api.logger.*;

import javax.swing.JFrame;
import com.sample.UI;

/**
 * This is a sample class to launch a rule.
 */
public class DroolsTest {

    public static final void main(String[] args) {
        try {
	        KieServices ks = KieServices.Factory.get();
    	    KieContainer kContainer = ks.getKieClasspathContainer();
        	KieSession kSession = kContainer.newKieSession("ksession-rules");
        	KieRuntimeLogger kLogger = ks.getLoggers().newFileLogger(kSession, "gui_debug");
        	
        	// Create the frame
            JFrame frame = new JFrame("What species did you evolve from?");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(600, 800); 
        	
            UI ui = new UI(frame, kLogger);

        	kSession.setGlobal("ui", ui);
        	
        	ui.initScreen(kSession);
        	
            } catch (Throwable t) {
            t.printStackTrace();
        }
    }

}