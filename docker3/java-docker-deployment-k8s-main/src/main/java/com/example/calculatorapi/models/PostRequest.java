/**
 * Post Request Class that maps the arithmetic request from the client
 * @author Nihinlolamiwa Fajemilehin
 */

package com.example.calculatorapi.models;

public class PostRequest {
	String operator;
	String firstValue;
	String secondValue;
	
	/**
	 * Function that returns the arithmetic operator
	 * @return The arithmetic operator
	 */
	public String getOperator() {
		return operator;
	}
	
	/**
	 * Function that returns the first arithmetic operand
	 * @return The The first arithmetic operand
	 */
	public String getFirstValue() {
		return firstValue;
	}
	
	/**
	 * Function that returns the second arithmetic operand
	 * @return The The second arithmetic operand
	 */
	public String getSecondValue() {
		return secondValue;
	}

	/**
	 * Function that sets the arithmetic operator
	 * @param operator
	 */
	public void setOperator(String operator) {
		this.operator = operator;
	}
	
	/**
	 * Function that sets the first arithmetic operand
	 * @param firstValue
	 */
	public void setFirstValue(String firstValue) {
		this.firstValue = firstValue;
	}
	
	/**Function that sets the second arithmetic operand
	 * @param secondValue
	 */
	public void setSecondValue(String secondValue) {
		this.secondValue = secondValue;
	}
}
