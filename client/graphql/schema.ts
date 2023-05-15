export const GetToken = gql`
	mutation tokenAuth($email: String!, $password: String!) {
		tokenAuth(email: $email, password: $password) {
			refreshExpiresIn
			token
			payload
			refreshToken
		}
	}
`;

export const RegisterUser = gql`
	mutation RegisterUser($email: String!, $fullName: String!, $password1: String!, $password2: String!) {
		registerUser(input: { email: $email, fullName: $fullName, password1: $password1, password2: $password2 }) {
			appUser {
				id
				email
				fullName
			}
			errors {
				field
				messages
			}
		}
	}
`;
