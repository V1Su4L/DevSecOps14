/**
 * The web controller class that houses the WEB API logic 
 * @author Nihinlolamiwa Fajemilehin
 */

package com.example.calculatorapi.controller;

import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import com.example.calculatorapi.models.PostRequest;
import com.example.calculatorapi.models.SquareRootRequest;
import com.example.calculatorapi.models.PostResponse;

@RestController
public class WebController {

	/**
	 * The Calculator Function that takes a PostRequest object, and performs the
	 * calculation and returns the response back to the client as a PostResponse
	 * object
	 * 
	 * @param inputPayload The PostRequest object received from the client
	 * @return The result of the arithmetic calculation
	 */
	@RequestMapping(value = "/calculate", method = RequestMethod.POST)
	public PostResponse Calculator(@RequestBody PostRequest inputPayload) {
		PostResponse response = new PostResponse();
		double result;
		try {
			// Validate the input values
			if (inputPayload.getOperator().isEmpty() || inputPayload.getOperator() == null) {
				response.setId(401);
				response.setError("Operator cannot be empty!");
				return response;
			} else if (inputPayload.getFirstValue().isEmpty() || inputPayload.getFirstValue() == null) {
				response.setId(401);
				response.setError("First Operand cannot be empty!");
				return response;
			} else if (inputPayload.getSecondValue().isEmpty() || inputPayload.getSecondValue() == null) {
				response.setId(401);
				response.setError("Second Operand cannot be empty!");
				return response;
			}

			// Perform calculation based on operator
			String operator = inputPayload.getOperator();
			switch (operator) {
			case "+":
				result = Double.parseDouble(inputPayload.getFirstValue())
						+ Double.parseDouble(inputPayload.getSecondValue());
				response.setId(200);
				response.setMessage(Double.toString(result));
				return response;
			case "-":
				result = Double.parseDouble(inputPayload.getFirstValue())
						- Double.parseDouble(inputPayload.getSecondValue());
				response.setId(200);
				response.setMessage(Double.toString(result));
				return response;
			case "÷":
				result = Double.parseDouble(inputPayload.getFirstValue())
						/ Double.parseDouble(inputPayload.getSecondValue());
				response.setId(200);
				response.setMessage(Double.toString(result));
				return response;
			case "x":
				result = Double.parseDouble(inputPayload.getFirstValue())
						* Double.parseDouble(inputPayload.getSecondValue());
				response.setId(200);
				response.setMessage(Double.toString(result));
				return response;
			default:
				result = 0;
				response.setId(999);
				response.setError("Operator passsed in not valid");
				return response;
			}
		} catch (Exception ex) {
			ex.getStackTrace();
			response.setId(401);
			response.setError("Fatal error occured!");
			return response;
		}
	}

	/**
	 * The SquareRoot Function that takes a PostRequest object, and performs the
	 * calculation and returns the response back to the client as a PostResponse
	 * object
	 * 
	 * @param inputPayload The SquareRootRequest object received from the client
	 * @return The result of the square root calculation
	 */
	@RequestMapping(value = "/squareroot", method = RequestMethod.POST)
	public PostResponse SquareRoot(@RequestBody SquareRootRequest inputPayload) {
		PostResponse response = new PostResponse();
		try {
			// Validate the input values
			if (inputPayload.getSquareRootOperand().isEmpty() || inputPayload.getSquareRootOperand() == null) {
				response.setId(401);
				response.setError("Square root operand cannot be empty!");
				return response;
			}
			// Perform calculation
			double squareRootValue = Math.sqrt(Double.parseDouble(inputPayload.getSquareRootOperand()));
			response.setId(200);
			response.setMessage(Double.toString(squareRootValue));
		} catch (Exception ex) {
			ex.getStackTrace();
			response.setId(401);
			response.setError("Fatal error occured!");
		}
		return response;
	}
}