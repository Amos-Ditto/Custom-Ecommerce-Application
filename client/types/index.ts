export interface IUserAuth {
	refreshExpiresIn: number;
	token: string;
	payload: IPayload;
	refreshToken: string;
}
export interface IPayload {
	email: string;
	exp: number;
	origIat: number;
}

export interface IRefreshToken {
	refreshExpiresIn: number;
	refreshToken: string;
}
