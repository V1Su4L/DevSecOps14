/**
 * Squareroot Request Class that maps the squareroot request from the client
 * @author Nihinlolamiwa Fajemilehin
 */

package com.example.calculatorapi.models;

public class SquareRootRequest {
	
	String squareRootOperand;
	
	/**
	 * Function that returns the squareroot operand
	 * @return The squareroot operand
	 */
	public String getSquareRootOperand() {
		return squareRootOperand;
	}

	/**
	 * Function that sets the squareroot operand
	 * @param squareRootOperand
	 */
	public void setSquareRootOperand(String squareRootOperand) {
		this.squareRootOperand = squareRootOperand;
	}
}
