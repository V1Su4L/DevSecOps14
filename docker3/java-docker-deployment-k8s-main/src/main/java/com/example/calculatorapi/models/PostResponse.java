/**
 * Post Response Class that maps the arithmetic calculation response back to the client
 * @author Nihinlolamiwa Fajemilehin
 */

package com.example.calculatorapi.models;

public class PostResponse {
	private String message;
	private long id;
	private String error;

	/**
	 * Function that returns the response message
	 * @return The response message
	 */
	public String getMessage() {
		return message;
	}

	/**
	 * Function that sets the response message
	 * @param message
	 */
	public void setMessage(String message) {
		this.message = message;
	}

	/**
	 * Function that returns the response ID
	 * @return The response ID
	 */
	public long getId() {
		return id;
	}

	/**
	 * Function that sets the response ID
	 * @param id
	 */
	public void setId(long id) {
		this.id = id;
	}

	/**
	 * Function that returns the response error
	 * @return The response error
	 */
	public String getError() {
		return error;
	}

	/**
	* Function that sets the response error
	 * @param error
	 */
	public void setError(String error) {
		this.error = error;
	}

}
